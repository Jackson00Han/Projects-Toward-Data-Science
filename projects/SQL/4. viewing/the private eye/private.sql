DROP TABLE IF EXISTS triplets;

CREATE TABLE triplets (
    id INTEGER PRIMARY KEY,
    sentence_id INTEGER NOT NULL,
    character_number INTEGER NOT NULL,
    message_length INTEGER NOT NULL
);

INSERT INTO triplets (sentence_id, character_number, message_length)
VALUES
(14, 98, 4),
(114, 3, 5),
(618, 72, 9),
(630, 7, 3),
(932, 12, 5),
(2230, 50, 7),
(2346, 44, 10),
(3041, 14, 5);

DROP VIEW IF EXISTS target_sentence;
CREATE VIEW target_sentence AS
SELECT t.sentence_id, s.sentence, t.character_number, t.message_length
FROM triplets t
LEFT JOIN sentences s ON t.sentence_id = s.id;

DROP VIEW IF EXISTS message;
CREATE VIEW message AS
SELECT substr(sentence, character_number, message_length) AS phrase
FROM target_sentence;


