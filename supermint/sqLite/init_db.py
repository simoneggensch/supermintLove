import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

# Open a cursor to perform database operations
cur = connection.cursor()


# create some quizzes
cur.execute('INSERT INTO quiz (title, round_titles, round_topics, google_slides_url, date_hosted)'
            'VALUES (?, ?, ?, ?, ?)',
            ('my first quiz',
             '{first_round, second_round}',
             '{Geography, History}',
             'fake_url.com',
             '2019-01-01')
            )

cur.execute('INSERT INTO quiz (title, round_titles, round_topics, google_slides_url, date_hosted)'
            'VALUES (?, ?, ?, ?, ?)',
            ('my second quiz',
             '{first_round, second_round}',
             '{Geography, History}',
             'fake_url1.com',
             '2020-01-02')
            )

cur.execute('INSERT INTO quiz (title, round_titles, round_topics, google_slides_url, date_hosted)'
            'VALUES (?, ?, ?, ?, ?)',
            ('my third quiz',
             '{first_round, second_round}',
             '{Geography, History}',
             'fake_url2.com',
             '2023-01-03')
            )

cur.execute('INSERT INTO quiz (title, round_titles, round_topics, google_slides_url, date_hosted)'
            'VALUES (?, ?, ?, ?, ?)',
            ('my third quiz',
             '{first_round, second_round}',
             '{Geography, History}',
             'fake_url3.com',
             '2024-01-04')
            )

# Create QuizLocations
cur.execute('INSERT INTO quiz_location (name)'
            'VALUES (?)',
            (('McCarthys',))
            )

cur.execute('INSERT INTO quiz_location (name)'
            'VALUES (?)',
            (('Giraf',))
            )


# Create some users
cur.execute('INSERT INTO user (first_name, last_name, pseudonym, email)'
            'VALUES (?, ?, ?, ?)',
            ('Simon',
             'Eggenschwiler',
             'me',
             'me@gmail.com')
            )

cur.execute('INSERT INTO user (first_name, last_name, pseudonym, email)'
            'VALUES (?, ?, ?, ?)',
            ('Etienne',
             'Batori',
             'you',
             'you@gmail.com')
            )

cur.execute('INSERT INTO user (first_name, last_name, pseudonym, email)'
            'VALUES (?, ?, ?, ?)',
            ('Meg',
             'Pitt',
             'Mumu',
             'megi@gmail.com')
            )

cur.execute('INSERT INTO user (first_name, last_name, pseudonym, email)'
            'VALUES (?, ?, ?, ?)',
            ('Bobo',
             'Momo',
             'Risbobo',
             'ris@gmail.com')
            )

# Link quizz to users in table author
cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('1',
             '1',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('1',
             '2',
             '1')
            )


cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('2',
             '3',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('2',
             '4',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('3',
             '1',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('3',
             '2',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('3',
             '3',
             '1')
            )

cur.execute('INSERT INTO author (quiz_id, user_id, quiz_location_id)'
            'VALUES (?, ?, ?)',
            ('4',
             '4',
             '1')
            )

connection.commit()

cur.close()
connection.close()
