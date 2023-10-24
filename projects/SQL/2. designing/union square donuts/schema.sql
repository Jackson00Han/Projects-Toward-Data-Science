CREATE TABLE "ingredients" (
    "id" INTEGER PRIMARY KEY,
    "ingredient" TEXT NOT NULL UNIQUE,
    "price_per" NUMERIC(10, 2) NOT NULL,
    "unit" TEXT NOT NULL
);


CREATE TABLE "donuts" (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "gluten_free" INTEGER CHECK("gluten_free" IN (0, 1)),
    "cost" NUMERIC(10, 2) NOT NULL,
    "unit" TEXT NOT NULL
);

CREATE TABLE "donut_ingredients" (
    "donut_id" INTEGER NOT NULL,
    "ingredient_id" INTEGER NOT NULL,
    PRIMARY KEY("donut_id", "ingredient_id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE "orders" (
    "id" INTEGER PRIMARY KEY,
    "order_number" INTEGER NOT NULL UNIQUE,
    "customer_id" INTEGER NOT NULL,
    FOREIGN KEY("customer_id") REFERENCES "customers"("id")
);

CREATE TABLE "order_donuts" (
    "order_id" INTEGER NOT NULL,
    "donut_id" INTEGER NOT NULL,
    "n_donuts" INTEGER NOT NULL,
    PRIMARY KEY("order_id", "donut_id"),
    FOREIGN KEY("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY("donut_id") REFERENCES "donuts"("id")
);

CREATE TABLE "customers" (
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL
);