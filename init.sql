CREATE TABLE Person (
    person_id SERIAL PRIMARY KEY,
    person_code VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
	surname VARCHAR(255) NOT NULL,
	patronymic VARCHAR(255),
    birth_date DATE NOT NULL,
    region VARCHAR(100),
    city VARCHAR(100),
    street VARCHAR(100),
    house VARCHAR(20),
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    clone_code VARCHAR(20) DEFAULT '5416'
);

CREATE TABLE Account (
    account_id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL REFERENCES Person(person_id) ON DELETE CASCADE,
    organization_code VARCHAR(20) NOT NULL,
    login VARCHAR(100) UNIQUE NOT NULL,
    password_hash BYTEA NOT NULL,
    registration_date TIMESTAMP DEFAULT NOW(),
    status SMALLINT NOT NULL DEFAULT 2,
    unique (person_id, organization_code)
);