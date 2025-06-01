# python-form-
a simple python program with mysql to take username and password from users and store them in the mysql database 
follow these steps 

step 1:
open mysql workbench and create a database with this command

"
CREATE DATABASE user_data;

USE user_data;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"

step 2:
install the mysql connector python library using pip

"
pip install mysql-connector-python
"

step 3:
in python code change user and password with your mysql username and password

for more detailed explanation of code see the pdf file attached with this code