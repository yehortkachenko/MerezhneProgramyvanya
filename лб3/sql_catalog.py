import sqlite3
conn = sqlite3.connect('catalog_egor.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS catalog (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price TEXT NOT NULL
)
''')
items = [
    (1, 'Espresso', '100'),
    (2, 'Cappuccino', '80.00'),
    (3, 'Americano', '50.00')
]
cursor.executemany('INSERT INTO catalog (id, name, price) VALUES (?, ?, ?)', items)
conn.commit()
conn.close()