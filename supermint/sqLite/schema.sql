DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS topic;
DROP TABLE IF EXISTS quiz_location;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS round;




CREATE TABLE IF NOT EXISTS location (id INTEGER PRIMARY KEY,
                                 name text NOT NULL
                                );


CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY,
                                 title text NOT NULL,
                                 location_id INTEGER NOT NULL,
                                 google_slides_url text,
                                 date_hosted date,
                                 date_added date DEFAULT CURRENT_TIMESTAMP,
                                 FOREIGN KEY(location_id) REFERENCES location(id)
                                );


CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                                 first_name text NOT NULL,
                                 last_name text NOT NULL,
                                 pseudonym text NOT NULL
                                );


CREATE TABLE IF NOT EXISTS topic (id INTEGER PRIMARY KEY,
                                 name text NOT NULL UNIQUE
                                );


CREATE TABLE IF NOT EXISTS author (id INTEGER PRIMARY KEY,
                                 quiz_id INTEGER NOT NULL,
                                 user_id INTEGER NOT NULL,
                                 FOREIGN KEY(quiz_id) REFERENCES quiz(id),
                                 FOREIGN KEY(user_id) REFERENCES user(id)
                                );


CREATE TABLE IF NOT EXISTS round (id INTEGER PRIMARY KEY,
                                 name text,
                                 description text DEFAULT '',
                                 round_number INTEGER NOT NULL,
                                 quiz_id INTEGER NOT NULL,
                                 topic_id INTEGER NOT NULL,
                                 FOREIGN KEY(quiz_id) REFERENCES quiz(id),
                                 FOREIGN KEY(topic_id) REFERENCES topic(id)
                                );
