create table if not exists users(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	surname VARCHAR(255) NOT NULL,
	patronymic VARCHAR(255),
	hashed_password VARCHAR(500) NOT NULL,
	email VARCHAR(500) NOT NULL
)
