CREATE TABLE amp.messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
