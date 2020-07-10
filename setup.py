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

noun = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in nouns])
adjective = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in adjectives])
github = "https://github.com/shardic1/li.nk"
t = (noun+adjective, github,)

conn = sql.connect("links.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS links
			(key TEXT, url TEXT)""")
c.execute("""INSERT INTO links (key, url)
			VALUES (?, ?)""", t)
conn.commit()
conn.close()