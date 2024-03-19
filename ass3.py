import psycopg2

def connect_db():
    # Connect to the PostgreSQL database with given credentials
    return psycopg2.connect(
        dbname="Student",
        user="postgres",
        password="asdf",
        host="localhost",
        port="5432"
    )

def getAllStudents():
    # Retrieve all student records from the database
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    students = cur.fetchall()
    for student in students:
        print(student)
    

def addStudent(first_name, last_name, email, enrollment_date):
    # Add a new student record to the database
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))
    conn.commit()


def updateStudentEmail(student_id, new_email):
    # Update the email address for a specific student
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()


def deleteStudent(student_id):
    # Delete a student record from the database
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()

    


# Example usage
if __name__ == "__main__":
    getAllStudents()
    # addStudent('Sahil', 'Far', 'sahil.far@example.com', '2023-10-01')
    # updateStudentEmail(1, 'johonny.updated@example.com')
    # deleteStudent(7)
