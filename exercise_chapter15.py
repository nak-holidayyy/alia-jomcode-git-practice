from pathlib import Path
from contextlib import closing
import sqlite3
import sys

example_1 = """WITH workshops(id, title, capacity) AS (
    VALUES ('w1', 'python', 20), ('w2','SQL', 5)
)
SELECT title, capacity FROM workshops
WHERE capacity >= 10 ORDER BY title"""
print("\nWORKED EXAMPLE 1: Safe SQL practice data")
with closing(sqlite3.connect(":memory:")) as connection:
    rows = connection.execute(example_1).fetchall()
assert rows == [("python", 20)]
print(rows)