CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    user_name VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);

CREATE TABLE schools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type ENUM('PRIMARY', 'Secondary', 'Higher Education') NOT NULL,
    location VARCHAR(255) NOT NULL,
    year SMALLINT UNSIGNED NOT NULL
);

CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry ENUM('Technology', 'Education', 'Business') NOT NULL,
    location VARCHAR(255) NOT NULL
);

CREATE TABLE connections (
    user_id INT NOT NULL,
    connection_id INT NOT NULL,
    PRIMARY KEY(user_id, connection_id)
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (connection_id) REFERENCES users(id)
);

CREATE TABLE connection_schools (
    user_id INT UNIQUE NOT NULL,
    school_id INT UNIQUE NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    degree ENUM('BA', 'MA', 'PHD') NOT NULL,
    PRIMARY KEY(user_id, school_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE con_companies (
    user_id INT NOT NULL,
    company_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    PRIMARY KEY(user_id, company_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (company_id) REFERENCES companies(id)
);