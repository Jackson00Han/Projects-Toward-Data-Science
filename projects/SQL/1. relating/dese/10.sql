SELECT d.name AS district_name, e.per_pupil_expenditure
FROM districts d
JOIN expenditures e ON d.id = e.district_id
WHERE d.type LIKE "%Public School%"
ORDER BY e.per_pupil_expenditure DESC
LIMIT 10