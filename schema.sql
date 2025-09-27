-- 1. Create the database
CREATE DATABASE attendance_db;

-- 2. Switch to the database
USE attendance_db;

-- 3. Create the attendance table
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    date DATE
);

-- 4. Verify
SHOW TABLES;
DESCRIBE attendance;
