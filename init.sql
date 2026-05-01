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

-- ENUM'ы
DO $$ BEGIN CREATE TYPE community_type_enum AS ENUM ('KLUB','KOOP','KUST','DELO','SOYUZ','INFO'); EXCEPTION WHEN duplicate_object THEN NULL; END $$;
DO $$ BEGIN CREATE TYPE community_status_enum AS ENUM ('draft','active','paused','closed','archived'); EXCEPTION WHEN duplicate_object THEN NULL; END $$;
DO $$ BEGIN CREATE TYPE membership_status_enum AS ENUM ('active','paused','left'); EXCEPTION WHEN duplicate_object THEN NULL; END $$;


-- community
CREATE TABLE IF NOT EXISTS community (
    community_id          integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    community_type        community_type_enum NOT NULL,
    name                  text NOT NULL,
    purpose               text NOT NULL,
    status                community_status_enum NOT NULL DEFAULT 'draft',
    created_at            timestamptz NOT NULL DEFAULT now(),
    CHECK (name <> ''),
    CHECK (purpose <> '')
);

-- membership
CREATE TABLE IF NOT EXISTS membership (
    membership_id         integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    person_id             integer NOT NULL REFERENCES person(person_id) ON DELETE CASCADE,
    community_id          integer NOT NULL REFERENCES community(community_id) ON DELETE CASCADE,
    joined_at             timestamptz NOT NULL DEFAULT now(),
    status                membership_status_enum NOT NULL DEFAULT 'active',
    left_at               timestamptz,
    CHECK ((status = 'left' AND left_at IS NOT NULL) OR (status <> 'left'))
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_membership_active
    ON membership(person_id, community_id)
    WHERE status = 'active';