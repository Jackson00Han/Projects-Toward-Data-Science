SELECT districts.name AS district_name
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
WHERE districts.name NOT LIKE "%(non-op)%"
AND expenditures.pupils = (
    SELECT MIN(pupils) FROM expenditures
)
ORDER BY district_name ASC;