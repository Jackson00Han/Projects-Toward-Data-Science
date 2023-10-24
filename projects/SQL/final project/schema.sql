-- Assuming all underlying data has been imported into the database with the help of Python.


DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS stocks;
DROP TABLE IF EXISTS extreme;
DROP INDEX IF EXISTS company_id_index;
DROP INDEX IF EXISTS name_index;
DROP INDEX IF EXISTS date_index;

CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    name VARCHAR(128) NOT NULL UNIQUE,
    ticker_symbol VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE stocks (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL,
    date DATE NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);


CREATE TABLE extreme_2023 (
    id INTEGER PRIMARY KEY,
    company_id INTEGER UNIQUE,
    min_open REAL,
    max_open REAL,
    min_close REAL,
    max_close REAL,
    max_volume REAL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE INDEX company_id_index ON stocks(company_id);
CREATE INDEX name_index ON companies(name);
CREATE INDEX date_index ON stocks(date);




