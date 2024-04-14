import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

# Open a cursor to perform database operations
cur = connection.cursor()

cur.execute('INSERT INTO quiz (title, authors, round_titles, round_topics)'
            'VALUES (?, ?, ?, ?)',
            ('my first quiz',
             '{me, you}',
             '{first_round, second_round}',
             '{Geography, History}')
            )

cur.execute('INSERT INTO quiz (title, authors, round_titles, round_topics)'
            'VALUES (?, ?, ?, ?)',
            ('my second quiz',
             '{Mégane, Boris}',
             '{first_round, second_round}',
             '{Geography, History}')
            )

connection.commit()

cur.close()
connection.close()
