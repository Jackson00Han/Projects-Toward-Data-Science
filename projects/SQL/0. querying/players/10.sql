SELECT first_name, last_name, bats as 'which side the player bats on'
FROM players
WHERE birth_country like 'USA'
ORDER BY first_name, last_name