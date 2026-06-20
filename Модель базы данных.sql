CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(150) NOT NULL UNIQUE,
    "last_name" varchar(150) NOT NULL,
    "email" varchar(254) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL,
    "first_name" varchar(150) NOT NULL
    );

CREATE TABLE "App_application" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "transport_type" varchar(20) NOT NULL,
    "start_date" date NOT NULL,
    "payment_method" varchar(20) NOT NULL,
    "status" varchar(20) NOT NULL,
    "created_at" datetime NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
    );

CREATE TABLE "App_profile" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "fio" varchar(255) NOT NULL,
    "birth_date" date NOT NULL,
    "phone" varchar(20) NOT NULL,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
    );