-- migrate:up

CREATE VIEW history AS
	SELECT
		log_date,
		TO_CHAR(weight / 1000.0, '999.9') AS kilos
	FROM logs
	ORDER BY log_date DESC;

-- migrate:down


DROP VIEW history;