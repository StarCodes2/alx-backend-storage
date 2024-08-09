-- Creates table users if it doesn't exist, with id set as primary key and auto increment, id and email as unique
CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255));
