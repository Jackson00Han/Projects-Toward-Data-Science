SELECT s.name AS school_name
FROM schools s
JOIN districts d ON s.district_id = d.id
WHERE d.city = 'Cambridge' AND d.type = 'Public School District';
