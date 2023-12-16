insert_today = """INSERT INTO logs
	(weight)
	VALUES
	(%(weight_in_grams)s)"""

history = """SELECT *
FROM history"""
