insert_today = """INSERT INTO logs
    (weight)
    VALUES
    (%(weight_in_grams)s)"""

history = """SELECT *
FROM history"""

recent_history = """SELECT *
FROM history
WHERE log_date >= CURRENT_DATE - 30"""
