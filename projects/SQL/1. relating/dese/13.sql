SELECT schools.name AS school_name, districts.name AS district_name, graduation_rates.dropped
FROM graduation_rates
JOIN schools ON graduation_rates.school_id = schools.id
JOIN districts ON schools.district_id = districts.id
ORDER BY graduation_rates.dropped ASC, district_name ASC, school_name ASC;