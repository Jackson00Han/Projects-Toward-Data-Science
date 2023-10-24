SELECT s.salary
FROM salaries s
WHERE player_id IN (
    SELECT p.player_id
    FROM performances p
    WHERE p.year = 2001
    AND p.HR = (
        SELECT MAX(HR)
        FROM performances
        WHERE year = 2001
    )
)
AND s.year = 2001;