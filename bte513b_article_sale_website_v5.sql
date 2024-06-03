-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 26, 2023 at 08:36 PM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bte513b_article_sale_website`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
CREATE TABLE IF NOT EXISTS `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_surname` varchar(50) DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `user_name`, `user_surname`, `user_email`) VALUES
(1, 'del', 'piero', 'delpiero@juve.com'),
(2, 'sen', 'abdulhamitleri', 'savundun@hot.com'),
(3, 'John', 'Wiley', 'wiley@hot.com'),
(4, 'kelly', 'brook', 'brook@hot.com'),
(5, 'senabdulhamitleri', 'savundum', 'hayir@savunmadim.com'),
(6, 'johndoe', 'Doe', 'johndoe@example.com'),
(7, 'janedoe', 'Doe', 'janedoe@example.com'),
(8, 'bobsmith', 'Smith', 'bobsmith@example.com'),
(9, 'lisajohnson', 'Johnson', 'lisajohnson@example.com'),
(10, 'mikesmith', 'Smith', 'mikesmith@example.com'),
(11, 'Ceren', 'Can', 'ceren@can.com'),
(12, 'Fracesco', 'Totti', 'totti@roma.com'),
(13, 'Francesco', 'Totti', 'totti@juve.com');

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
CREATE TABLE IF NOT EXISTS `articles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `article_title` varchar(100) DEFAULT NULL,
  `article_year` int DEFAULT NULL,
  `journal_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `journal_id` (`journal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `article_title`, `article_year`, `journal_id`) VALUES
(2, 'nano', 1222, 3),
(3, 'nano3', 1224, 4),
(4, 'nanno', 1925, 2),
(5, 'nanoono', 1900, 4),
(6, 'nano', 1222, 3),
(7, 'nano', 1222, 3),
(8, 'NANO TECH', 1985, 5),
(9, 'Quantum Physics', 2020, 6),
(10, 'Artificial Intelligence', 2022, 7),
(11, 'Renewable Energy', 2019, 8),
(12, 'Nanotechnology', 2018, 9),
(13, 'Robotics', 2021, 10),
(14, 'Neuroscience', 2020, 6),
(15, 'Data Science', 2017, 7),
(16, 'Otonom Araçların Teknoloji Kabul Modulune Gore Incelenmesi', 2022, 11),
(19, 'nano', 1222, 3),
(23, 'nanooooo5', 1222, 3),
(24, 'nano', 21551, 12),
(25, 'NANO TECH BY ROBOTS', 1222, 3),
(26, 'NANOTECH BY HUMANS', 1222, 3),
(27, 'NANOTECH BY SENTIENTS', 1999, 13),
(28, 'NANOTECH and Biomimicy', 2020, 13);

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
CREATE TABLE IF NOT EXISTS `authors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author_name` varchar(50) DEFAULT NULL,
  `author_surname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`id`, `author_name`, `author_surname`) VALUES
(1, 'John', 'Doe'),
(2, 'as', 'ds'),
(3, 'franz', 'totti'),
(4, 'didier', 'drogba'),
(5, 'seedorf', 'cle'),
(6, 'pao', 'maldini'),
(7, 'ahmet', 'mehmet'),
(8, 'maldini', 'mardini'),
(9, 'kanadali', 'jameson'),
(10, 'EVET', 'SAVUNDUM'),
(11, 'John', 'Doe'),
(12, 'Jane', 'Doe'),
(13, 'Robert', 'Smith'),
(14, 'Lisa', 'Johnson'),
(15, 'Mike', 'Smith'),
(16, 'Emily', 'Anderson'),
(17, 'David', 'Williams'),
(18, 'Sophia', 'Brown'),
(19, 'Daniel', 'Garcia'),
(20, 'Olivia', 'Martinez'),
(21, 'Beliz', 'Cakir'),
(22, 'Ceren', 'Yolal'),
(23, 'asgfasgasg', 'asgfasg'),
(24, 'Beliz', 'Can'),
(25, 'didier', 'beliz'),
(26, 'Cafu', 'Andre'),
(27, 'Brezilyali', 'Kaka');

-- --------------------------------------------------------

--
-- Table structure for table `author_order`
--

DROP TABLE IF EXISTS `author_order`;
CREATE TABLE IF NOT EXISTS `author_order` (
  `article_id` int DEFAULT NULL,
  `author_id` int DEFAULT NULL,
  `author_order` int DEFAULT NULL,
  KEY `article_id` (`article_id`),
  KEY `author_id` (`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `author_order`
--

INSERT INTO `author_order` (`article_id`, `author_id`, `author_order`) VALUES
(2, 4, 1),
(3, 7, 1),
(3, 4, 1),
(4, 8, 1),
(4, 7, 2),
(5, 9, 1),
(2, 2, 1),
(9, 13, 1),
(10, 14, 1),
(11, 15, 1),
(12, 16, 1),
(13, 17, 1),
(14, 18, 1),
(15, 19, 1),
(12, 18, 2),
(15, 19, 2),
(19, 4, 1),
(23, 4, 1),
(24, 23, 1),
(25, 24, 1),
(26, 25, 1),
(27, 25, 1),
(28, 26, 1),
(28, 27, 2);

-- --------------------------------------------------------

--
-- Table structure for table `journals`
--

DROP TABLE IF EXISTS `journals`;
CREATE TABLE IF NOT EXISTS `journals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `journal_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `journals`
--

INSERT INTO `journals` (`id`, `journal_name`) VALUES
(1, 'ASME'),
(2, 'ASME2'),
(3, 'ASME3'),
(4, 'ASME5'),
(5, 'ASME7'),
(6, 'Science Journal'),
(7, 'Technology Review'),
(8, 'Nature'),
(9, 'Engineering Today'),
(10, 'AI & Robotics'),
(11, 'ITU Kutuphane Yayinlari'),
(12, 'gfaga'),
(13, 'ASME9');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
CREATE TABLE IF NOT EXISTS `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `article_id` int DEFAULT NULL,
  `sale_date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `article_id` (`article_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `user_id`, `article_id`, `sale_date`) VALUES
(3, 1, 5, '2023-12-24 22:58:38'),
(4, 1, 2, '2023-12-26 00:05:02'),
(5, 11, 15, '2023-12-26 15:38:29'),
(6, 12, 28, '2023-12-26 20:07:32');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `articles`
--
ALTER TABLE `articles`
  ADD CONSTRAINT `articles_ibfk_1` FOREIGN KEY (`journal_id`) REFERENCES `journals` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `author_order`
--
ALTER TABLE `author_order`
  ADD CONSTRAINT `author_order_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `author_order_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `accounts` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
