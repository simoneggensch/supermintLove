import sqlite3
import os

os.remove("database.db")
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

# Open a cursor to perform database operations
cur = connection.cursor()


# Create QuizLocations
cur.executemany('INSERT INTO location (name)'
            'VALUES (?)',
            [
                ('McCarthys',),
                ('Giraf',)
            ]
            )


# Create round topics
cur.executemany('INSERT INTO topic (name)'
            'VALUES (?)',
            [
                ('Geography',),
                ('History',),
                ('MovieSeries',),
                ('Guesstimate',),
                ('Other',)
            ]
            )


# create some quizzes
cur.executemany('INSERT INTO quiz (title, location_id, google_slides_url, date_hosted)'
            'VALUES (?, ?, ?, ?)',
            [
                ('my first quiz',
                '1',
                'fake_url.com',
                '2019-01-01'),

                ('my second quiz',
                '1',
                'fake_url1.com',
                '2020-01-02'),

                ('my third quiz',
                '1',
                'fake_url2.com',
                '2023-01-03'),
                
                ('my third quiz',
                '1',
                'fake_url3.com',
                '2024-01-04')
            ]
            )

cur.executemany('INSERT INTO round (name, description, round_number, quiz_id, topic_id)'
                'VALUES (?, ?, ?, ?, ?)',
                [
                    ('first round', 'first description of a round', '1', '1', '1'),
                    ('second round', 'second description of a round', '2', '1', '2'),
                    ('Movies & Series', 'This describes movies', '1', '2', '3'),
                    ('Guess guess', 'brief', '2', '2', '4'),
                    ('round 3', 'first description of a round', '3', '2', '5'),
                    ('round 1', 'first description of a round', '1', '3', '1'),
                    ('round 2', 'first description of a round', '2', '3', '1'),
                    ('round 3', 'first description of a round', '3', '3', '1')
                ]
                )

cur.executemany('INSERT INTO round (name, round_number, quiz_id, topic_id)'
                'VALUES (?, ?, ?, ?)',
                [
                    ('first round', '1', '4', '1'),
                    ('second round', '2', '4', '1'),
                    ('third round', '3', '4', '1'),
                    ('fourth round', '4', '4', '1'),
                    ('fifth round', '5', '4', '1'),
                ]
                )

# Create some users
cur.executemany('INSERT INTO user (first_name, last_name, pseudonym)'
            'VALUES (?, ?, ?)',
            [
                ('Simon',
                'Eggenschwiler',
                'me'),
                
                ('Etienne',
                'Batori',
                'you'),

                ('Meg',
                'Pitt',
                'Mumu'),

                ('Bobo',
                'Momo',
                'Risbobo')
            ]
            )

# Link quizz to users in table author
cur.executemany('INSERT INTO author (quiz_id, user_id)'
            'VALUES (?, ?)',
            [
                ('1', '1'),
                ('1', '2'),
                ('2', '3'),
                ('2', '4'),
                ('3', '1'),
                ('3', '2'),
                ('3', '3'),
                ('4', '4')
            ]
            )

connection.commit()

cur.close()
connection.close()
