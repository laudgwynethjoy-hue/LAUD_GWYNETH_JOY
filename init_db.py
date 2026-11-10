import sqlite3

DATABASE = "students.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create the table for a new database.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'Local'
)
""")

# Migrate an existing Activity 7/8 database without deleting records.
columns = [row[1] for row in cursor.execute("PRAGMA table_info(students)").fetchall()]
if "source" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN source TEXT DEFAULT 'Local'")

cursor.execute("""
UPDATE students
SET source = 'Local'
WHERE source IS NULL OR TRIM(source) = ''
""")

# Add starter records only when the database is empty.
count = cursor.execute("SELECT COUNT(*) FROM students").fetchone()[0]

if count == 0:
    students = [
        ('2026-00146', 'Princess Grace Patricio', 'BSIT', 3, 'C', 'Local'),
        ('2026-00147', 'KC Jane Marie Ladoing', 'BSIT', 2, 'A', 'Local'),
        ('2026-00148', 'Yvonne Mahilum', 'BSIT', 1, 'B', 'Local'),
        ('2026-00149', 'Lay Mae Sumido', 'BSOA', 2, 'A', 'Local'),
        ('2026-00150', 'Neca Mae Herbaliga', 'BSIT', 3, 'B', 'Local')
    ]

    cursor.executemany("""
        INSERT INTO students (student_id, name, program, year, section, source)
        VALUES (?, ?, ?, ?, ?, ?)
    """, students)

conn.commit()
conn.close()

print("Database is ready. Existing student records were preserved.")
