CREATE TABLE "passenger" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INTEGER NOT NULL
);

CREATE TABLE "airlines" (
    "id" INTEGER PRIMARY KEY,
    "airline_name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT CHECK (concourse IN ('A', 'B', 'C', 'D', 'E', 'F', 'T'))
);

CREATE TABLE "flights" (
    "id" INTEGER PRIMARY KEY,
    "flight_number" INTEGER NOT NULL,
    "airline_id" INTEGER NOT NULL,
    "departure" TEXT NOT NULL,
    "heading" TEXT NOT NULL,
    "departure_date_time" TEXT NOT NULL,
    "arrival_date_time" TEXT NOT NULL,
    FOREIGN KEY("airline_id") REFERENCES "airlines"("id")
);

CREATE TABLE "check_ins" (
    "id" INTEGER PRIMARY KEY,
    "passenger_id" INTEGER NOT NULL,
    "date_time" TEXT NOT NULL,
    "flight_id" INTEGER NOT NULL,
    FOREIGN KEY("passenger_id") REFERENCES "passenger"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id")
)

