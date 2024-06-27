import sqlite3

websites = ["https://google.com", "https://facebook.com", "https://twitter.com"]

conn = sqlite3.connect('websites.db')
cursor = conn.cursor()

for site in websites:
    cursor.execute('''
    INSERT INTO websites (url, status) VALUES (?, 'UNKNOWN')
    ''', (site,))

conn.commit()
conn.close()

print("Дані успішно додані до таблиць")