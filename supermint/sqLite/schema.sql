DROP TABLE IF EXISTS quiz;

CREATE TABLE IF NOT EXISTS quiz (id serial PRIMARY KEY,
                                 title text NOT NULL,
                                 authors text[],
                                 round_titles  text[],
                                 round_topics,
                                 date_added date DEFAULT CURRENT_TIMESTAMP);

