SELECT t.name
FROM teams t
WHERE id IN (
    SELECT DISTINCT team_id
    FROM performances
    WHERE player_id IN (
        SELECT id
        FROM players
        WHERE first_name LIKE '%Satchel%'
        AND last_name LIKE '%Paige%'
    )
);
