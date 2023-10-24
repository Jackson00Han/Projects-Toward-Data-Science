SELECT city, COUNT(name)
FROM (
    SELECT name, city
    FROM schools
    WHERE type LIKE "Public School"
)
GROUP BY city
ORDER BY COUNT(name) DESC, city ASC
LIMIT 10;