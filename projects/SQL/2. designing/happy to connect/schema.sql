CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL
);

CREATE TABLE "schools" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INTEGER NOT NULL
);

CREATE TABLE "companies" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL
);

CREATE TABLE "connections" (
    "id" INTEGER PRIMARY KEY,
    "user_id" INTEGER NOT NULL,
    "connection_people_id" INTEGER,
    "connection_school_id" INTEGER,
    "school_start_date" TEXT,
    "school_end_date" TEXT,
    "degree" TEXT NOT NULL,
    "connection_company_id" INTEGER,
    "company_start_date" TEXT,
    "company_end_date" TEXT,
    "title" TEXT NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("connection_people_id") REFERENCES "users"("id"),
    FOREIGN KEY ("connection_school_id") REFERENCES "schools"("id"),
    FOREIGN KEY ("connection_company_id") REFERENCES "companies"("id")
)