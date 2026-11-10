
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL
)
''')

# Clear previous records
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='students'")

# Five sample student records
students = [
    ('2026-00146', 'Princess Grace Patricio', 'BSIT', 3, 'C'),
    ('2026-00147', 'KC Jane Marie Ladoing', 'BSIT', 2, 'A'),
    ('2026-00148', 'Yvonne Mahilum', 'BSIT', 1, 'B'),
    ('2026-00149', 'Lay Mae Sumido', 'BSOA', 2, 'A'),
    ('2026-00150', 'Neca Mae Herbaliga', 'BSIT', 3, 'B')
]

# Insert records into database
cursor.executemany('''
INSERT INTO students (student_id, name, program, year, section)
VALUES (?, ?, ?, ?, ?)
''', students)

# Save and close database
conn.commit()
conn.close()

print("Database created successfully.")
