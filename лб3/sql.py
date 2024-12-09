import sqlite3
conn = sqlite3.connect('users_egor.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ("admin", "admin123"))
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ("user", "user123"))
conn.commit()
conn.close()
