



SELECT first_name, last_name
FROM (
    SELECT pl.id, pl.first_name, pl.last_name, (s.salary / pe.RBI) AS "dollars per RBI"
    FROM players pl
    JOIN performances pe ON pl.id = pe.player_id
    JOIN salaries s ON pl.id = s.player_id
    WHERE s.year = pe.year
    AND s.year = 2001
    AND pe.RBI <> 0
    ORDER BY "dollars per RBI" ASC, pl.first_name ASC, pl.last_name ASC
    LIMIT 10
) x
NATURAL JOIN (
    SELECT pl.id, pl.first_name, pl.last_name, (s.salary / pe.H) AS "dollars per hit"
    FROM players pl
    JOIN performances pe ON pl.id = pe.player_id
    JOIN salaries s ON pl.id = s.player_id
    WHERE s.year = pe.year
    AND s.year = 2001
    AND pe.H <> 0
    ORDER BY "dollars per hit" ASC, pl.first_name ASC, pl.last_name ASC
    LIMIT 10
) y
ORDER BY x.id ASC
