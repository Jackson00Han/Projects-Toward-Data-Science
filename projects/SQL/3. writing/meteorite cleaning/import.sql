DROP TABLE IF EXISTS meteorites_temp;
CREATE TABLE meteorites_temp (
    name TEXT,
    id INTEGER,
    nametype TEXT,
    class TEXT,
    mass REAL,
    discovery TEXT,
    year REAL,
    lat REAL,
    long REAL
);

.import --csv --skip 1 meteorites.csv meteorites_temp

DELETE FROM meteorites_temp WHERE nametype LIKE 'Relict';

UPDATE meteorites_temp
SET
    mass = CASE WHEN mass = '' THEN NULL ELSE ROUND(mass, 2) END,
    year = NULLIF(year, ''),
    lat = CASE WHEN lat = '' THEN NULL ELSE ROUND(lat, 2) END,
    long = CASE WHEN long = '' THEN NULL ELSE ROUND(long, 2) END;

DROP TABLE IF EXISTS meteorites;

CREATE TABLE meteorites (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    mass REAL,
    discovery TEXT CHECK (discovery IN ('Fell', 'Found')),
    year REAL,
    lat REAL,
    long REAL
);

INSERT INTO meteorites (name, class, mass, discovery, year, lat, long) -- Removed nametype
SELECT name, class, mass, discovery, year, lat, long
FROM meteorites_temp
ORDER BY year ASC, name ASC;

DROP TABLE meteorites_temp;