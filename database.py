import sqlite3
import random
import names


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        matric_no TEXT,
        grade TEXT,
        tcp INTEGER,
        tnu INTEGER,
        gpa REAL,
        remarks TEXT
    )
    """)
    conn.commit()


def insert_dummy_data(conn):
    cursor = conn.cursor()
    remarks_options = ['Excellent', 'Good', 'Fair', 'Poor']

    for i in range(5):
        name = names.get_full_name()
        matric_no = f'MAT{i:03}'
        grade = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        tcp = random.randint(10, 25)
        tnu = random.randint(18, 20)
        gpa = round(tcp / tnu, 2)
        remarks = random.choice(remarks_options)

        cursor.execute("""
        INSERT INTO students (name, matric_no, grade, tcp, tnu, gpa, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, matric_no, grade, tcp, tnu, gpa, remarks))

    conn.commit()


def display_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("Name\t\tMatric No.\tGrade\tTCP\tTNU\tGPA\tRemarks")
    print("-" * 80)

    for row in rows:
        print(f"{row[1]}\t{row[2]}\t\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}")


def delete_data(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE students")

db_file = "students.db"
conn = create_connection(db_file)
# create_table(conn)
insert_dummy_data(conn)
# display_data(conn)
# delete_data(conn)
display_data(conn)
conn.close()