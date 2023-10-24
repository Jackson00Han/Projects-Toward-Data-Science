SELECT
    t.name AS "team name",
    SUM(p.H) AS "total hits"
FROM
    teams t
JOIN
    performances p ON t.id = p.team_id
WHERE
    p.year = 2001
GROUP BY
    p.team_id
ORDER BY
    SUM(p.H) DESC
LIMIT 5;
