CREATE DATABASE IF NOT EXISTS ${MYSQL_DATABASE};

USE ${MYSQL_DATABASE};

-- Inventory table with location and recall status fields
CREATE TABLE IF NOT EXISTS inventory (
  id INT AUTO_INCREMENT PRIMARY KEY,
  barcode VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  quantity INT DEFAULT 0,
  location VARCHAR(255) DEFAULT 'default_location',  -- Location of the item
  is_recalled BOOLEAN DEFAULT FALSE  -- Recalled status of the item
);

-- Users table for authentication (optional)
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password_hash VARCHAR(255) NOT NULL
);

-- Any further alterations to the schema can go here
