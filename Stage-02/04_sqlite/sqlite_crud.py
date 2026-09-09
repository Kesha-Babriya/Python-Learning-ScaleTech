import sqlite3

#connect with database 

connection = sqlite3.connect("students.db")

print("connection successfully done")

#cursor for execute sql commands
cursor = connection.cursor()

#create table 
cursor.execute('''
             CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT
            )
    ''')    

#add into table
def add_student(name ,grade):
    cursor.execute('''
        INSERT INTO students (name,grade) VALUES(?,?) ''',
        (name,grade))
    print(f"student {name} added successfully")

#fetch data from table
def fetch():
    cursor.execute('''
        SELECT * FROM students''')
    many_fetch = cursor.fetchmany(2)        #it fetches first 2 rows
    data = cursor.fetchall()
    for row in data:
        print(row)

#update table
def update(name ,grade):
    cursor.execute('''
        UPDATE students 
        SET grade = ?
        WHERE name = ?''',
        (grade,name))

#delete data from table

def delete(name):
    cursor.execute('''
    DELETE FROM students
    WHERE name = ? 
    ''' ,(name,))           # wants tuple not value

add_student('kesha','A')
add_student('Rubby','B')
add_student('kia','C')

print("After add, see table")
print(fetch())

update('Rubby','A+')
delete('kia')

print("After update and delete , table contains: ")
print(fetch())

connection.commit()

#close database connection
connection.close()