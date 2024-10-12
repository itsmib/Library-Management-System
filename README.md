Library Management System
This is a simple Library Management System built using Python and MySQL. The project allows administrators to add, display, and delete book records from a library database.
Prerequisites
Before you can run this project, make sure you have the following installed:
- Python 3.x
- MySQL Server
- Python packages:
  - `mysql-connector-python`
  - `tabulate`

You can install the required Python packages using:
pip install mysql-connector-python tabulate
Setting Up the MySQL Database
1. Create a MySQL Database:

Open the MySQL command line or a MySQL GUI like phpMyAdmin and run the following command to create a new database:
CREATE DATABASE library;
2. Create Tables:

Use the following SQL commands to create the required tables in the `library` database.
Create `STAFF_LIBRARY` table:
CREATE TABLE STAFF_LIBRARY (
    BOOK_ID VARCHAR(10) PRIMARY KEY,
    TITLE VARCHAR(30),
    AUTHOR VARCHAR(30),
    ISBN VARCHAR(20),
    STAFF_ID VARCHAR(10),
    STAFF_NAME VARCHAR(30),
    BORROW_DATE DATE,
    RETURN_DATE DATE
);
Create `STUDENT_LIBRARY` table:
CREATE TABLE STUDENT_LIBRARY (
    BOOK_ID VARCHAR(10) PRIMARY KEY,
    TITLE VARCHAR(30),
    AUTHOR VARCHAR(30),
    ISBN VARCHAR(20),
    STUDENT_ID VARCHAR(10),
    STUDENT_NAME VARCHAR(30),
    BORROW_DATE DATE,
    RETURN_DATE DATE
);

3. Insert Sample Data (Optional):
Insert Data into `STAFF_LIBRARY`:
INSERT INTO STAFF_LIBRARY (BOOK_ID, TITLE, AUTHOR, ISBN, STAFF_ID, STAFF_NAME, BORROW_DATE, RETURN_DATE) VALUES 
('BKID-1', 'The Great Gatsby', 'F. Scott Fitzgerald', '978-0743273565', 'STF-101', 'John Doe', '2022-01-01', '2022-02-01');

Insert Data into `STUDENT_LIBRARY`:
INSERT INTO STUDENT_LIBRARY (BOOK_ID, TITLE, AUTHOR, ISBN, STUDENT_ID, STUDENT_NAME, BORROW_DATE, RETURN_DATE) VALUES 
('BKID-101', 'The Alchemist', 'Paulo Coelho', '978-0061122415', 'STD-001', 'Misbah', '2022-03-12', '2022-03-19');

Configuring the Python Script
1. Clone the Repository:
Clone this repository to your local machine:
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System
2. Update Database Connection:
Open the Python file (`your_python_file.py`) and update the MySQL connection details with your username, password, host, and database name:
conn = mysql.connector.connect(
    user='your_username', 
    password='your_password', 
    host='localhost', 
    database='library'
)
Running the Project
To run the project, execute the Python file:
python your_python_file.py
How to Use
1. Choose a Library:
   When you run the program, you will be asked to select either the Student Library or Staff Library.
2. View Records:
   Choose the option to view all records in the selected library.
3. Add a New Record:
   Input the details like `BOOK_ID`, `TITLE`, `AUTHOR`, `ISBN`, `STUDENT_ID`/`STAFF_ID`, `STUDENT_NAME`/`STAFF_NAME`, `BORROW_DATE`, and `RETURN_DATE`.
4. Delete a Record:
   Provide the `BOOK_ID` of the record you want to delete.
5. Exit:
   Select the option to quit the program.
   
License
This project is licensed under the MIT License - see the LICENSE file for details.
