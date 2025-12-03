CREATE DATABASE IF NOT EXISTS `assignment-5`;
USE `assignment-5`;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  age INT
);

INSERT INTO users (username, email, age) VALUES
('ahmed', 'ahmed@gmail.com', 26),
('peter', 'peter@gmail.com', 30),
('alex', 'alex@gmail.com', 28);
