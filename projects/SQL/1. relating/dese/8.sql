SELECT districts.name AS district_name, expenditures.pupils AS enrolled_pupils
FROM districts
JOIN expenditures ON districts.id = expenditures.district_id
WHERE districts.name NOT LIKE "%(non-op)%"
ORDER BY enrolled_pupils DESC, district_name ASC