-- migrate:up

CREATE TABLE logs (
	log_date DATE PRIMARY KEY DEFAULT CURRENT_DATE,
	weight INTEGER
);


-- migrate:down

DROP TABLE logs;