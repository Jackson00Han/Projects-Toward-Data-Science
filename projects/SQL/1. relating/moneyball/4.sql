SELECT first_name, last_name, s.salary
FROM players p
JOIN salaries s ON p.id = s.player_id
WHERE s.year = 2001
ORDER BY s.salary ASC, first_name, last_name, p.id
LIMIT 50