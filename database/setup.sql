-- Create the 'odm2' schema
CREATE SCHEMA "odm2";

-- Create the 'agriculturalparcel' table within the 'odm2' schema
CREATE TABLE "odm2"."agriculturalparcel" (
    "id" SERIAL PRIMARY KEY,
    "farm_name" VARCHAR(255) NOT NULL,
    "plot_name" VARCHAR(255) NOT NULL
);

-- Note: The 'public' schema is created by default in PostgreSQL.
