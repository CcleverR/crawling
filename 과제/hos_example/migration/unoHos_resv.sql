CREATE TABLE `doctor` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `hospital` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `major` varchar(20) NOT NULL,
  `specialization` varchar(128),
  `contacts` varchar(255),
  `created_at` timestamp DEFAULT (now()),
  `deleted_at` timestamp
);