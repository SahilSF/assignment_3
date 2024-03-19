Author - Sahil sirajuddin Farooqui
Student ID - 101284858

Youtube Link - https://youtu.be/zFwm9ebGGJE

1. Install module using - pip install psycopg2

2. Create a table in PorstgreSQL using:

    CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

3. Insert data using:

    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');


4. Change the connection credentials:

    dbname="your_database_name"
    user="your_database_username"
    password="your_database_password"
    host="localhost" (or your database host)
    port="5432" (or your database port)

5. To compile the python file:

    python3 ass3.python

6. Run the query using pgAdmin to check if the changes are made
