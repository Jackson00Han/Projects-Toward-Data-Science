
-- Define Common Table Expressions (CTEs) for Apple and Exxon Mobil Corp's data in 2023
WITH
    apple AS (
        SELECT
            ROW_NUMBER() OVER (ORDER BY date DESC) AS id,
            date, open, high, low, close, volume
        FROM stocks
        WHERE company_id = (
            SELECT id
            FROM companies
            WHERE name = 'Apple'
        )
        AND date LIKE '2023%'
    ),
    xom AS (
        SELECT
            ROW_NUMBER() OVER (ORDER BY date DESC) AS id,
            date, open, high, low, close, volume
        FROM stocks
        WHERE company_id = (
            SELECT id
            FROM companies
            WHERE name = 'Exxon Mobil Corp'
        )
        AND date LIKE '2023%'
    )

-- Insert extreme values into the extreme table for both companies


-- Calculate mean close price for both companies
SELECT AVG(close) AS 'mean close price of Apple in 2023' FROM apple;
SELECT AVG(close) AS 'mean close price of XOM in 2023' FROM xom;

-- Calculate variance of close price for both companies
SELECT
    AVG(
        (close - (SELECT AVG(close) FROM apple)) *
        (close - (SELECT AVG(close) FROM apple))
    ) AS 'close price variance of Apple in 2023'
FROM
    apple;

SELECT
    AVG(
        (close - (SELECT AVG(close) FROM xom)) *
        (close - (SELECT AVG(close) FROM xom))
    ) AS 'close price variance of XOM in 2023'
FROM
    xom;

-- Calculate Simple Moving Average over 3 consecutive days for both companies
WITH JoinAppleData AS (
    SELECT a.id AS id,
           a.date AS date,
           a.close AS close0,
           b.close AS close1,
           c.close AS close2
    FROM apple a
    LEFT JOIN apple b ON a.id = b.id - 1
    LEFT JOIN apple c ON a.id = c.id - 2
)
SELECT id,
       date,
       ROUND(
        (close0 + COALESCE(close1, 0) + COALESCE(close2, 0)) /
       (1 + CASE WHEN close1 IS NULL THEN 0 ELSE 1 END + CASE WHEN close2 IS NULL THEN 0 ELSE 1 END)
       , 2) AS APPLE_SMA_3_day
FROM JoinAppleData
ORDER BY date DESC;

WITH JoinXomData AS (
    SELECT a.id AS id,
           a.date AS date,
           a.close AS close0,
           b.close AS close1,
           c.close AS close2
    FROM xom a
    LEFT JOIN xom b ON a.id = b.id - 1
    LEFT JOIN xom c ON a.id = c.id - 2
)
SELECT id,
       date,
       ROUND(
        (close0 + COALESCE(close1, 0) + COALESCE(close2, 0)) /
       (1 + CASE WHEN close1 IS NULL THEN 0 ELSE 1 END + CASE WHEN close2 IS NULL THEN 0 ELSE 1 END)
       , 2) AS XOM_SMA_3_day
FROM JoinXomData
ORDER BY date DESC;
;
