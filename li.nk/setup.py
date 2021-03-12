"""
	setup.py

	creates the necessary database file
	and initialises it with random
	values
"""

import sqlite3 as sql
import random

adjectives = open("adjectives.txt", "r")
nouns = open("nouns.txt", "r")

# noun = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in nouns])
# adjective = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in adjectives])

# Random noun and adjective collected from files
noun = ""
adjective = ""

# Random line number
n_line = random.randint(0, 10)
a_line = random.randint(11, 20)

# GitHub link
github = "https://github.com/shardic1/li.nk"

# Collect random noun from nouns file
while nouns and n_line:
    noun = next(nouns).rstrip().rstrip("\n").lstrip()
    n_line -= 1

# Collect random adjective from adjectives file
while adjectives and a_line:
    adjective = next(adjectives).rstrip().rstrip("\n").lstrip()
    a_line -= 1

# Tuple pair of random key and url
t = (adjective+noun, github,)

# Store key-url pair in SQL database
conn = sql.connect("links.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS links
			(key TEXT, url TEXT)""")
c.execute("""INSERT INTO links (key, url)
			VALUES (?, ?)""", t)
conn.commit()

# Cleanup
conn.close()
nouns.close()
adjectives.close()
