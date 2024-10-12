import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(user='misbah', password='1234', host='localhost', database='library')
c = conn.cursor()

def cho():
    print('\nSelect an option:')
    print('1. View all records')
    print('2. Add a new record')
    print('3. Delete a record')
    print('4. Quit')
    print()
    ch = int(input('Enter choice: '))
    return ch

def std_lib():
    while True:
        ch = cho()
        if ch == 1:
            c.execute('SELECT * FROM STUDENT_LIBRARY')
            rows = c.fetchall()
            headers = ['BOOK_ID', 'TITLE', 'AUTHOR', 'ISBN', 'STUDENT_ID', 'STUDENT_NAME', 'BORROW_DATE', 'RETURN_DATE']
            table = tabulate(rows, headers, tablefmt='psql')
            print(table)
        if ch == 2:
            BOOK_ID = input('Enter book ID : ')
            TITLE = input('Enter book title : ')
            AUTHOR = input('Enter the author name : ')
            ISBN = input('Enter the ISBN.NO : ')
            STUDENT_ID = input('Enter the STUDENT ID : ')
            STUDENT_NAME = input('Enter the STUDENT NAME : ')
            BORROW_DATE = input("Enter the borrow date (YYYY-MM-DD): ")
            RETURN_DATE = input("Enter the return date (YYYY-MM-DD): ")
            c.execute('INSERT INTO STUDENT_LIBRARY (BOOK_ID, TITLE, AUTHOR, ISBN, STUDENT_ID, STUDENT_NAME, BORROW_DATE, RETURN_DATE) VALUES (%s, %s, %s,%s, %s, %s,%s,%s)', (BOOK_ID, TITLE, AUTHOR, ISBN, STUDENT_ID, STUDENT_NAME, BORROW_DATE, RETURN_DATE))
            conn.commit()
            print("The Following Field is added")
        if ch == 3:
            BOOK_ID = input('Enter BOOK ID that you want to delete : ')
            c.execute('DELETE FROM STUDENT_LIBRARY WHERE BOOK_ID = %s', (BOOK_ID,))
            conn.commit()
            print("The Following Field is Deleted")
        if ch == 4:
            break
        cn = input("DO YOU WANT TO CONTINUE : ")
        if cn != 'y' and cn != 'Y':
            break

def staff_lib():
    while True:
        ch = cho()
        if ch == 1:
            c.execute('SELECT * FROM STAFF_LIBRARY')
            rows = c.fetchall()
            headers = ['BOOK_ID', 'TITLE', 'AUTHOR', 'ISBN', 'STAFF_ID', 'STAFF_NAME', 'BORROW_DATE', 'RETURN_DATE']
            table = tabulate(rows, headers, tablefmt='psql')
            print(table)
        if ch == 2:
            BOOK_ID = input('Enter book ID : ')
            TITLE = input('Enter book title : ')
            AUTHOR = input('Enter the author name : ')
            ISBN = input('Enter the ISBN.NO : ')
            STAFF_ID = input('Enter the STAFF ID : ')
            STAFF_NAME = input('Enter the STAFF NAME : ')
            BORROW_DATE = input("Enter the borrow date (YYYY-MM-DD): ")
            RETURN_DATE = input("Enter the return date (YYYY-MM-DD): ")
            c.execute('INSERT INTO STAFF_LIBRARY (BOOK_ID, TITLE, AUTHOR , ISBN, STAFF_ID, STAFF_NAME, BORROW_DATE, RETURN_DATE) VALUES (%s, %s, %s,%s, %s, %s,%s,%s)', (BOOK_ID, TITLE, AUTHOR, ISBN, STAFF_ID, STAFF_NAME, BORROW_DATE, RETURN_DATE))
            conn.commit()
            print("field added")
        if ch == 3:
            BOOK_ID = input('Enter BOOK ID that you want to delete : ')
            c.execute('DELETE FROM STAFF_LIBRARY WHERE BOOK_ID = %s', (BOOK_ID,))
            conn.commit()
            print("The Following Field is Deleted")
        if ch == 4:
            break
        cn = input("DO YOU WANT TO CONTINUE : ")
        if cn != 'y' and cn != 'Y':
            break

while True:
    print("Which library would you like to access?")
    print("1. Student Library")
    print("2. Staff Library")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You have accessed the student library.")
        std_lib()
        break
    elif choice == "2":
