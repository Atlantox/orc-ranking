-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: WikiwikiExample.mysql.pythonanywhere-services.com    Database: WikiwikiExample$orc_ranking
-- ------------------------------------------------------
-- Server version	5.7.44-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `binnacle`
--

DROP TABLE IF EXISTS `binnacle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `binnacle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `action` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ip_address` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `binnacle_user` (`user`),
  CONSTRAINT `binnacle_user` FOREIGN KEY (`user`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=261 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binnacle`
--

LOCK TABLES `binnacle` WRITE;
/*!40000 ALTER TABLE `binnacle` DISABLE KEYS */;
INSERT INTO `binnacle` VALUES (218,10,'Atlantox ha ingresado al sistema','2024-08-16 19:30:38','10.0.5.105'),(219,10,'Creó al jugador Gwen','2024-08-16 19:30:49','10.0.5.105'),(220,10,'Atlantox ha ingresado al sistema','2024-08-18 02:38:56','10.0.5.105'),(221,10,'Atlantox ha ingresado al sistema','2024-08-18 02:51:20','10.0.5.105'),(222,10,'Creó el torneo del día 2024-08-10','2024-08-18 02:55:31','10.0.5.105'),(223,10,'Creó al jugador Gerardo','2024-08-18 23:14:10','10.0.5.105'),(224,10,'Creó al jugador Ricardo','2024-08-18 23:14:20','10.0.5.105'),(225,10,'Creó al jugador Angel Virgüez','2024-08-18 23:14:32','10.0.5.105'),(226,10,'Creó al jugador Leonardo','2024-08-18 23:14:46','10.0.5.105'),(227,10,'Creó al jugador Mark','2024-08-18 23:14:56','10.0.5.105'),(228,10,'Creó al jugador Alexander','2024-08-18 23:15:06','10.0.5.105'),(229,10,'Creó el deck Alela, Cunning Conqueror','2024-08-18 23:15:39','10.0.5.105'),(230,10,'Creó el deck Atarka, World Render','2024-08-18 23:16:10','10.0.5.105'),(231,10,'Creó el deck Kruphix, God of Horizons','2024-08-18 23:16:41','10.0.5.105'),(232,10,'Creó el deck Voja, Jaws Of The Conclave','2024-08-18 23:17:17','10.0.5.105'),(233,10,'Creó el deck Jhoira, Ageless Innovator','2024-08-18 23:17:46','10.0.5.105'),(234,10,'Creó el deck Astarion, the Decadent','2024-08-18 23:18:39','10.0.5.105'),(235,10,'Creó el deck Balmor, Battlemage Captain','2024-08-18 23:19:20','10.0.5.105'),(236,10,'Creó el deck Olivia, Opulent Outlaw','2024-08-18 23:19:45','10.0.5.105'),(237,10,'Creó el torneo del día 2024-08-18','2024-08-18 23:24:09','10.0.5.105'),(238,10,'Creó al jugador Daniel Ganzo','2024-08-25 23:58:34','10.0.5.105'),(239,10,'Creó al jugador Nandy','2024-08-25 23:58:44','10.0.5.105'),(240,10,'Creó al jugador Miguel','2024-08-25 23:58:51','10.0.5.105'),(241,10,'Creó al jugador Gabriel','2024-08-25 23:59:06','10.0.5.105'),(242,10,'Creó el deck Kykar, Wind\'s Fury','2024-08-26 00:00:09','10.0.5.105'),(243,10,'Creó el deck Leori, Sparktouched Hunter','2024-08-26 00:01:14','10.0.5.105'),(244,10,'Creó el deck Keleth + Tevesh','2024-08-26 00:02:27','10.0.5.105'),(245,10,'Creó el deck Animar, Soul of Elements','2024-08-26 00:03:14','10.0.5.105'),(246,10,'Creó el deck Krenko, Tin Street Kingpin','2024-08-26 00:03:50','10.0.5.105'),(247,10,'Creó el deck Minsc & Boo, Timeless Heroes','2024-08-26 00:04:32','10.0.5.105'),(248,10,'Modificó el deck \"4\"','2024-08-26 00:04:59','10.0.5.105'),(249,10,'Creó el torneo del día 2024-08-25','2024-08-26 00:10:27','10.0.5.105'),(250,10,'Modificó el deck \"5\"','2024-08-26 00:10:50','10.0.5.105'),(251,10,'Modificó el deck \"10\"','2024-08-26 00:11:18','10.0.5.105'),(252,10,'Creó el deck Emmara, Soul of the Accord','2024-09-01 22:45:07','10.0.5.105'),(253,10,'Creó el deck The Scarab God','2024-09-01 22:45:35','10.0.5.105'),(254,10,'Creó el deck Tayam, enigma resplandeciente','2024-09-01 22:46:33','10.0.5.105'),(255,10,'Creó al jugador Katsura','2024-09-01 22:47:07','10.0.5.105'),(256,10,'Creó al jugador Nelson','2024-09-01 22:47:14','10.0.5.105'),(257,10,'Creó el torneo del día 2024-09-01','2024-09-01 22:52:25','10.0.5.105'),(258,10,'Creó al jugador Ricardo Mendoza','2024-09-01 23:05:15','10.0.5.105'),(259,10,'Renombró al jugador \"Ricardo\" por \"Ricardo Dragones\" ','2024-09-01 23:05:29','10.0.5.105'),(260,10,'Modificó el deck \"29\"','2024-09-02 00:12:43','10.0.5.105');
/*!40000 ALTER TABLE `binnacle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `color`
--

DROP TABLE IF EXISTS `color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `color` (
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color`
--

LOCK TABLES `color` WRITE;
/*!40000 ALTER TABLE `color` DISABLE KEYS */;
INSERT INTO `color` VALUES ('Azul'),('Blanco'),('Incoloro'),('Negro'),('Rojo'),('Verde');
/*!40000 ALTER TABLE `color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deck`
--

DROP TABLE IF EXISTS `deck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deck` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deck`
--

LOCK TABLES `deck` WRITE;
/*!40000 ALTER TABLE `deck` DISABLE KEYS */;
INSERT INTO `deck` VALUES (13,'Alela, Cunning Conqueror'),(24,'Animar, Soul of Elements'),(18,'Astarion, the Decadent'),(14,'Atarka, World Render'),(19,'Balmor, Battlemage Captain'),(12,'Ellivere of the Wild Court'),(27,'Emmara, Soul of the Accord'),(2,'Ertai Resurrected'),(5,'Horde of Notions'),(17,'Jhoira, Ageless Innovator'),(23,'Keleth + Tevesh'),(25,'Krenko, Tin Street Kingpin'),(15,'Kruphix, God of Horizons'),(21,'Kykar, Wind\'s Fury'),(22,'Leori, Sparktouched Hunter'),(26,'Minsc & Boo, Timeless Heroes'),(9,'Mogis, God of Slaugther -Tax Life'),(8,'Octavia, Living thesis'),(11,'Okinec -Aggro'),(20,'Olivia, Opulent Outlaw'),(3,'Purphoros, Bronze-Blooded'),(6,'Sliver Overlord'),(29,'Tayam, Luminous Enigma'),(4,'Thalia and The Gitrog Monster'),(10,'The necrobloom'),(28,'The Scarab God'),(1,'Umbris, fear manifest'),(16,'Voja, Jaws Of The Conclave');
/*!40000 ALTER TABLE `deck` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deck_color`
--

DROP TABLE IF EXISTS `deck_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deck_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deck` int(11) NOT NULL,
  `color` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deck_color_deck` (`deck`),
  KEY `deck_color_color` (`color`),
  CONSTRAINT `deck_color_color` FOREIGN KEY (`color`) REFERENCES `color` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `deck_color_deck` FOREIGN KEY (`deck`) REFERENCES `deck` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deck_color`
--

LOCK TABLES `deck_color` WRITE;
/*!40000 ALTER TABLE `deck_color` DISABLE KEYS */;
INSERT INTO `deck_color` VALUES (1,1,'Azul'),(2,1,'Negro'),(3,2,'Azul'),(5,2,'Negro'),(6,5,'Azul'),(7,5,'Blanco'),(8,5,'Negro'),(9,5,'Rojo'),(10,5,'Verde'),(16,6,'Blanco'),(17,6,'Verde'),(18,6,'Azul'),(19,6,'Rojo'),(20,6,'Negro'),(26,3,'Rojo'),(27,4,'Blanco'),(28,4,'Negro'),(29,4,'Verde'),(33,8,'Azul'),(34,9,'Negro'),(35,9,'Rojo'),(36,10,'Blanco'),(37,10,'Verde'),(38,10,'Negro'),(39,11,'Blanco'),(40,11,'Verde'),(41,12,'Verde'),(42,12,'Blanco'),(43,13,'Negro'),(44,13,'Azul'),(45,14,'Verde'),(46,14,'Rojo'),(47,15,'Azul'),(48,15,'Verde'),(49,16,'Verde'),(50,16,'Rojo'),(51,16,'Blanco'),(52,17,'Azul'),(53,17,'Rojo'),(54,18,'Negro'),(55,18,'Blanco'),(56,19,'Azul'),(57,19,'Rojo'),(58,20,'Negro'),(59,20,'Rojo'),(60,20,'Blanco'),(61,21,'Rojo'),(62,21,'Blanco'),(63,21,'Azul'),(64,22,'Rojo'),(65,22,'Blanco'),(66,22,'Azul'),(67,23,'Negro'),(68,23,'Blanco'),(69,24,'Rojo'),(70,24,'Verde'),(71,24,'Azul'),(72,25,'Rojo'),(73,26,'Rojo'),(74,26,'Verde'),(75,27,'Verde'),(76,27,'Blanco'),(77,28,'Azul'),(78,28,'Negro'),(79,29,'Verde'),(80,29,'Negro'),(81,29,'Blanco');
/*!40000 ALTER TABLE `deck_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_format`
--

DROP TABLE IF EXISTS `game_format`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_format` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_format`
--

LOCK TABLES `game_format` WRITE;
/*!40000 ALTER TABLE `game_format` DISABLE KEYS */;
INSERT INTO `game_format` VALUES (3,'Coliseo'),(5,'Coliseo Duel'),(2,'EDH'),(1,'Pauper');
/*!40000 ALTER TABLE `game_format` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisson`
--

DROP TABLE IF EXISTS `permisson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `permisson_user_level` (`level`),
  CONSTRAINT `permisson_user_level` FOREIGN KEY (`level`) REFERENCES `user_level` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisson`
--

LOCK TABLES `permisson` WRITE;
/*!40000 ALTER TABLE `permisson` DISABLE KEYS */;
INSERT INTO `permisson` VALUES (29,'Admin','Super'),(30,'Editor','Super'),(31,'Estadísticas','Super'),(32,'Jugadores','Super'),(33,'Mazos','Super'),(34,'Formatos','Super'),(35,'Temporadas','Super'),(36,'Torneos','Super'),(37,'Editor','Admin'),(38,'Jugadores','Admin'),(39,'Mazos','Admin'),(40,'Estadísticas','Admin'),(41,'Temporadas','Admin'),(42,'Formatos','Admin'),(43,'Torneos','Admin'),(44,'Mazos','Editor'),(45,'Jugadores','Editor'),(46,'Estadísticas','Editor'),(47,'Formatos','Editor'),(48,'Bitácora','Super'),(49,'Bitácora','Admin');
/*!40000 ALTER TABLE `permisson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (18,'Alexander'),(15,'Angel Virgüez'),(6,'Antoanel'),(9,'Atlantox'),(3,'Boros'),(19,'Daniel Ganzo'),(7,'Danny'),(22,'Gabriel'),(13,'Gerardo'),(12,'Gwen'),(23,'Katsura'),(16,'Leonardo'),(11,'Luis Lugo'),(8,'Manstrac'),(10,'Marcelo'),(17,'Mark'),(21,'Miguel'),(20,'Nandy'),(24,'Nelson'),(14,'Ricardo Dragones'),(25,'Ricardo Mendoza'),(2,'Roberto Suárez'),(1,'Yanez'),(4,'Yeshirler Rodríguez');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `season`
--

DROP TABLE IF EXISTS `season`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `season` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `season`
--

LOCK TABLES `season` WRITE;
/*!40000 ALTER TABLE `season` DISABLE KEYS */;
INSERT INTO `season` VALUES (1,'1','2024-08-16',1);
/*!40000 ALTER TABLE `season` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournament`
--

DROP TABLE IF EXISTS `tournament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournament` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `format` varchar(50) NOT NULL,
  `observation` varchar(200) NOT NULL,
  `season` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `pot` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`id`),
  KEY `tournament_season` (`season`),
  KEY `tournament_format` (`format`),
  CONSTRAINT `tournament_format` FOREIGN KEY (`format`) REFERENCES `game_format` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tournament_season` FOREIGN KEY (`season`) REFERENCES `season` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournament`
--

LOCK TABLES `tournament` WRITE;
/*!40000 ALTER TABLE `tournament` DISABLE KEYS */;
INSERT INTO `tournament` VALUES (2,'2024-08-18','Coliseo','',1,1,1.00),(3,'2024-08-25','Coliseo','',1,1,2.00),(4,'2024-09-01','Coliseo','',1,1,5.00);
/*!40000 ALTER TABLE `tournament` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournament_result`
--

DROP TABLE IF EXISTS `tournament_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournament_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tournament` int(11) NOT NULL,
  `player` int(11) NOT NULL,
  `deck` int(11) NOT NULL,
  `wins` decimal(4,2) NOT NULL,
  `winner` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tournament_result_player` (`player`),
  KEY `tournament_result_deck` (`deck`),
  KEY `tournament_result_tournament` (`tournament`),
  CONSTRAINT `tournament_result_deck` FOREIGN KEY (`deck`) REFERENCES `deck` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tournament_result_player` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tournament_result_tournament` FOREIGN KEY (`tournament`) REFERENCES `tournament` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournament_result`
--

LOCK TABLES `tournament_result` WRITE;
/*!40000 ALTER TABLE `tournament_result` DISABLE KEYS */;
INSERT INTO `tournament_result` VALUES (5,2,18,19,3.25,0),(6,2,15,15,2.33,0),(7,2,9,1,1.25,0),(8,2,7,17,3.91,0),(9,2,13,13,2.33,0),(10,2,12,20,1.33,0),(11,2,1,2,4.58,0),(12,2,2,4,2.33,0),(13,2,14,14,5.33,0),(14,2,17,18,8.33,0),(15,2,16,16,10.00,1),(16,2,10,12,0.00,0),(17,3,6,25,6.00,0),(18,3,18,19,6.33,0),(19,3,9,1,4.00,0),(20,3,1,2,10.00,0),(21,3,7,17,20.00,1),(22,3,19,21,0.00,0),(23,3,2,4,13.00,0),(24,3,15,15,5.00,0),(25,3,22,24,10.00,0),(26,3,4,5,2.00,0),(27,3,16,16,3.33,0),(28,3,20,22,0.00,0),(29,3,21,23,8.00,0),(30,3,12,20,5.00,0),(31,3,14,14,0.00,0),(32,3,13,13,0.00,0),(33,3,17,26,7.33,0),(34,4,6,25,2.00,0),(35,4,3,3,1.00,0),(36,4,7,17,5.00,0),(37,4,22,24,0.00,0),(38,4,21,23,5.00,0),(39,4,1,2,10.00,1),(40,4,25,27,5.00,0),(41,4,17,26,7.00,0),(42,4,23,28,5.00,0),(43,4,2,4,0.00,0),(44,4,24,29,5.00,0);
/*!40000 ALTER TABLE `tournament_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `token` varchar(200) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `username` (`username`),
  KEY `user_user_level` (`level`),
  CONSTRAINT `user_user_level` FOREIGN KEY (`level`) REFERENCES `user_level` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (10,'Atlantox','Super','2024-06-25 19:49:47','$argon2id$v=19$m=65536,t=3,p=4$am1VC7JJtJEwA6YHympJfA$g7uf84pTXJKeq5QsUGqDacFoj54gR35J9uwf9KFsX7M','$argon2id$v=19$m=65536,t=3,p=4$cb6WD/wlSRf4MIxzlJn/hA$0NKlEYkLPgRvStyq1NSLdJZtTaOMKLjizEdhJ9mrONU','dcd78902-70b4-40a2-9c17-b7a0486e9980-5f031834-7798-4cb4-a77b-114b3a7b8d6f',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_level`
--

DROP TABLE IF EXISTS `user_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_level` (
  `name` varchar(20) NOT NULL,
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_level`
--

LOCK TABLES `user_level` WRITE;
/*!40000 ALTER TABLE `user_level` DISABLE KEYS */;
INSERT INTO `user_level` VALUES ('Admin'),('Editor'),('Super');
/*!40000 ALTER TABLE `user_level` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-21  1:17:18
