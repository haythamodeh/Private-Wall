from flask import Flask, redirect, request, render_template, flash, session
from mysqlconnection import connectToMySQL
import re
import datetime
from flask_bcrypt import Bcrypt        


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "secret key"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wall")
def wall():
    if session["loggedin"] != True:
        flash("You must be logged in to enter this website", "loggedin")
        return redirect("/")
    else:
        mysql = connectToMySQL("userInfo")
        query = "SELECT id, first_name FROM userInfo.users WHERE first_name != %(fn)s;"
        data = {
            "fn": session["sendername"]
        }
        users = mysql.query_db(query,data)

        mysql = connectToMySQL("userInfo")
        query = """SELECT messages.id, messages.message, messages.created_at, messages.sendername FROM userInfo.messages
                    JOIN userInfo.users on messages.user_id = users.id 
                    WHERE users.id = %(id)s;"""
        data = {
            "id": session["id"]
        }
        messages = mysql.query_db(query,data)
        print(messages)
        return render_template("wall.html", users = users, messages = messages)

@app.route("/registerprocess", methods=["POST"])
def registerprocess():
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    confirmpassword = request.form["password_confirm"]
    is_valid = True

    if firstname == "" and lastname == "" and email == "" and password == "" and confirmpassword == "":
        is_valid = False
        flash("All fields are required", "message")
        return redirect("/")
    if firstname.isalpha() == False:
        is_valid = False
        flash("First Name must be letters only", "fn_error")
        return redirect("/")
    if len(firstname) < 2:
        is_valid = False
        flash("First Name must be more than 2 characters", "fn_error")
        return redirect("/")
    if lastname.isalpha() == False:
        is_valid = False
        flash("Last Name must be letters only", "ln_error")
        return redirect("/")
    if len(lastname) < 2:
        is_valid = False
        flash("First Name must be more than 2 characters", "ln_error")
        return redirect("/")
    if lastname.isalpha() == False:
        is_valid = False
        flash("Last Name must be letters only", "ln_error")
        return redirect("/")
    if email == "":
        is_valid = False
        flash("Email cannot be blank", "e_error")
    if not EMAIL_REGEX.match(email):    # test whether a field matches the pattern
        is_valid = False
        flash("Invalid email address!", "e_error")
        return redirect("/")    
    if len(password) < 8:
        is_valid = False
        flash("Password must be longer than 8 characters!", "p_error")
        return redirect("/")
    if password != confirmpassword:
        is_valid = False
        flash("Passwords don't match", "pc_error")
        return redirect("/")
    

    # check if email is in database, if it is return email has been taken otherwise put the values in the database
    mysql = connectToMySQL("userInfo")
    query = "SELECT email FROM userInfo.users WHERE email = %(email)s"
    data = {
        "email": email
    }
    getemail = mysql.query_db(query,data)
    print(getemail)
    if len(getemail) < 1:
        # if we reached here that means email is valid
        if is_valid:
            hashed_password = bcrypt.generate_password_hash(password)
            mysql = connectToMySQL("userInfo")
            query = "INSERT INTO userInfo.users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s,%(pw)s, NOW(), NOW());"
            data = {
                "fn": firstname,
                "ln": lastname,
                "email": email,
                "pw": hashed_password
            }
            mysql.query_db(query,data)
            session["loggedin"] = True
            session["name"] = firstname + " " + lastname
            session["sendername"] = firstname
            return redirect("/wall") 
    elif getemail[0]["email"] == email:
        is_valid = False
        flash("The email (" + email + ") has already been taken!", "e_error")
        return redirect("/")        

@app.route("/loginprocess", methods=["POST"])
def loginprocess():
    email = request.form["email"]
    password = request.form["password"]
    is_valid = True

    if email == "":
        is_valid = False
        flash("Email cannot be blank", "e_errorLogin")
    if not EMAIL_REGEX.match(email):    # test whether a field matches the pattern
        is_valid = False
        flash("Invalid email address!", "e_errorLogin")
        return redirect("/")    
    if len(password) < 1:
        is_valid = False
        flash("Password field must not be empty!", "p_error")
        return redirect("/")

    mysql = connectToMySQL("userInfo")
    query = "SELECT id, first_name, last_name, email, password FROM userInfo.users WHERE email = %(email)s;"
    data = {
        "email": email
    }
    getinfo = mysql.query_db(query,data)
    print(len(getinfo))
    if len(getinfo) >= 1:
        userid = getinfo[0]["id"]
        userfirstname = getinfo[0]["first_name"]
        userlastname = getinfo[0]["last_name"]
        useremail = getinfo[0]["email"]
        userhashpassword = getinfo[0]["password"]

    # print(userfirstname)
    # print(userlastname)
    # print(useremail)
    # print(userhashpassword)
    # print(getinfo)
    
    if len(getinfo) < 1:
        is_valid = False
        flash("You could not be logged in", "loggedin_error")
        return redirect("/")
    elif useremail == email and bcrypt.check_password_hash(userhashpassword, password) == False:
        is_valid = False
        flash("You could not be logged in", "loggedin_error")
        return redirect("/")
    elif useremail == email and bcrypt.check_password_hash(userhashpassword, password):
        is_valid = True
        session["loggedin"] = True
        session["sendername"] = userfirstname
        session["id"] = userid
        session["name"] = userfirstname + " " + userlastname
        return redirect("/wall")
    
@app.route("/logout")
def logout():
    session["loggedin"] = False
    flash("You have been logged out", "loggedin")
    return redirect("/")

@app.route("/sendMessageProcess", methods = ["POST"])
def sendMessageProcess():
    message = request.form["message"]
    recepientid = request.form["recepientid"]
    print(recepientid)
    print(message)
    print("*" *50)

    mysql = connectToMySQL("userInfo")
    query = "INSERT INTO userInfo.messages (message, created_at, updated_at, sendername, user_id) VALUES (%(msg)s, NOW(), NOW(), %(sendername)s, %(recepientid)s);"
    data = {
        "msg": message,
        "sendername": session["sendername"],
        "recepientid": recepientid   
    }
    ex = mysql.query_db(query,data)
    print(ex)
    flash("Message Successfully Sent!", "sentmessages")
    return redirect("/wall")
    
@app.route("/delete/<userid>")
def delete(userid):
    mysql = connectToMySQL("userInfo")
    query = "DELETE FROM userInfo.messages WHERE id = %(id)s;"
    data = {
        "id": userid
    }
    mysql.query_db(query,data)
    flash("Message Successfully Deleted", "incomingmessages")
    return redirect("/wall")

if __name__=="__main__":
    app.run(debug=True)