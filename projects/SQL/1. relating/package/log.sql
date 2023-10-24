
-- *** The Lost Letter ***
SELECT type, address FROM addresses
WHERE id IN (
        SELECT to_address_id FROM packages
        WHERE (
            from_address_id IN (
              SELECT id FROM addresses
              WHERE address LIKE "%900 Somerville Avenue%"
            )
            AND
            contents LIKE "%congratulatory%"
        )
);


-- *** The Devious Delivery ***


SELECT id, contents
FROM packages
WHERE (contents LIKE "%duck%" OR contents LIKE "%quack%")
AND from_address_id IS NULL;

SELECT address_id, action, timestamp
FROM scans
WHERE package_id = 5098;

SELECT type
FROM addresses
WHERE id = 348;
-- *** The Forgotten Gift ***
SELECT id, contents
FROM packages
WHERE from_address_id IN (
    SELECT id
    FROM addresses
    WHERE address LIKE "109 Tileston Street"
);

SELECT *
FROM scans
WHERE package_id = 9523;

SELECT address
FROM addresses
WHERE id = 7432;

SELECT name
FROM drivers
WHERE id = 17