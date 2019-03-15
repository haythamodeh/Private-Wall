CREATE DATABASE  IF NOT EXISTS `userInfo` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `userInfo`;
-- MySQL dump 10.13  Distrib 8.0.14, for macos10.14 (x86_64)
--
-- Host: localhost    Database: userInfo
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `sendername` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'hello john','2019-02-14 18:05:18','2019-02-14 18:05:18','haytham',2),(7,'hello world','2019-02-14 19:33:29','2019-02-14 19:33:29','john',1),(8,'hellow','2019-02-14 19:35:58','2019-02-14 19:35:58','john',1),(9,'','2019-02-14 19:36:29','2019-02-14 19:36:29','john',1),(10,'fgfd','2019-02-14 19:38:07','2019-02-14 19:38:07','john',1),(11,'ded','2019-02-14 19:40:32','2019-02-14 19:40:32','john',1),(12,'hr','2019-02-14 19:41:36','2019-02-14 19:41:36','john',1),(13,'','2019-02-14 19:42:09','2019-02-14 19:42:09','john',1),(14,'dfdsfdf','2019-02-14 19:43:59','2019-02-14 19:43:59','john',1),(15,'jjjkln','2019-02-14 19:44:39','2019-02-14 19:44:39','john',1),(16,'rert','2019-02-14 19:46:53','2019-02-14 19:46:53','john',1),(17,'ergre','2019-02-14 19:50:06','2019-02-14 19:50:06','john',1),(18,'fdkjhg','2019-02-14 19:52:28','2019-02-14 19:52:28','john',1),(19,'','2019-02-14 19:52:37','2019-02-14 19:52:37','john',1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'haytham','odeh','haythamlion@outlook.com','$2b$12$uvLwZCK/OASpnFkxGNDSROS2v5WGX1K/nIPnPj5cZqlqZYtjryNqq','2019-02-14 15:05:04','2019-02-14 15:05:04'),(2,'john','cena','john@email.com','$2b$12$jZNQrGs1P2prQlnk2eZeB.Fm/sAzuEJ39FKRg.hAIfJh/R86P/ffu','2019-02-14 16:19:18','2019-02-14 16:19:18'),(3,'dwayne','johnson','dwayne@email.com','$2b$12$ZSMSLFuiRe4WRfIX/qp10.VhBvgm.V8elGn0cc9vFn7gS5iOpOGs6','2019-02-14 16:20:01','2019-02-14 16:20:01');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-14 19:55:52
