SELECT pl.first_name AS "first_name", pl.last_name AS "last_name", s.salary AS "salary", s.year AS "year", pe.HR AS "HR"
FROM players pl
JOIN salaries s ON pl.id = s.player_id
JOIN performances pe ON pl.id = pe.player_id
WHERE s.year = pe.year
ORDER BY pl.id ASC, pe.year DESC, pe.HR DESC, s.salary DESC
