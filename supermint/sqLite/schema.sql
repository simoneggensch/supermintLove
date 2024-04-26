DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS host;
DROP TABLE IF EXISTS quizmaster;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS quiz_location;


CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY,
                                 title text NOT NULL,
                                 round_titles  text[],
                                 round_topics text[],
                                 google_slides_url text,
                                 date_hosted date,
                                 date_added date DEFAULT CURRENT_TIMESTAMP
                                );


CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                                 first_name text NOT NULL,
                                 last_name text NOT NULL,
                                 pseudonym text NOT NULL,
                                 email text
                                );


CREATE TABLE IF NOT EXISTS quiz_location (id INTEGER PRIMARY KEY,
                                 name text NOT NULL
                                );

CREATE TABLE IF NOT EXISTS author (id INTEGER PRIMARY KEY,
                                 quiz_id INTEGER NOT NULL,
                                 user_id INTEGER NOT NULL,
                                 quiz_location_id INTEGER NOT NULL,
                                 FOREIGN KEY(quiz_id) REFERENCES quiz(id),
                                 FOREIGN KEY(user_id) REFERENCES user(id),
                                 FOREIGN KEY(quiz_location_id) REFERENCES quiz_location(id)
                                );

