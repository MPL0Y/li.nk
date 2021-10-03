"""
	li.nk : A new way to shorten
	        your links.

	Author : @MPL0Y	
"""

# Uses Python's SQLite3 library for
# custom link database
import sqlite3 as sql
import random

# Connects the li.nk database
conn = sql.connect("links.db")

# Message for invalid choice
def invalid():
	print("Invalid choice.\n")
	main()

def append(key, url):
	global conn
	if (has_key(key)):
		raise Exception(f"li.nk/{key} is not available.")
	else:
		conn.execute(f"""INSERT INTO links (key, url)
	                   VALUES (?, ?);""", (key, url,))
		conn.commit()
		print("Your personal link is created!")
		print(f"{url} is now: li.nk/{key}")

def has_key(key):
	global conn
	# Efficient method to check key presence
	rows = conn.execute("""SELECT *
	                       FROM links
	                       WHERE key = ?
	                       LIMIT 1;""", (key,))
	exists = False
	# Check iterable of 'rows' for any element
	for r in rows:
		exists = True
		break
	return exists

# Check availability of a link
def check():
	global conn
	key = input("Enter a key to check: li.nk/")
	if (has_key(key)):
		print(f"li.nk/{key} is not available.\n")
	else:
		print(f"li.nk/{key} is available.\n")

# Avail random-generated link
def avail():
	global conn
	url = input("Enter your URL: ")
	# Generating random key for user
	# through an adjective+verb combination
	nouns = open("nouns.txt", "r")
	adjectives = open("adjectives.txt", "r")
	noun = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in nouns])
	adjective = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in adjectives])
	key = adjective + noun
	try:
		append(key, url)
	except Exception as e:
		print(e)

def avail_custom():
	global conn
	key = input("Enter your custom key: li.nk/")
	if (has_key(key)):
		print(f"li.nk/{key} is not available.")
	else:
		url = input("Enter your URL: ")
		try:
			append(key, url)
		except Exception as e:
			print(e)
			return
		print("Your personal link is created!")
		print(f"{url} is now: li.nk/{key}")

def remove():
	pass

def dump():
	global conn
	dump = conn.execute("""SELECT * FROM links;""")
	for d in dump:
		print(d)

def end():
	raise SystemExit

def main():

	print("Welcome to li.nk (URL SHORTENER)!\n")
	print("| MENU |\n")
	print("1. Check availability of link")
	print("2. Avail link")
	print("3. Avail custom link")
	print("4. Remove link")
	print("5. Exit")

	choice = input("Enter choice: ")

	funclist = {
		"1": "check()",
		"2": "avail()",
		"3": "avail_custom()",
		"4": "remove()",
		"5": "end()",
		"69": "dump()"
	}

	eval(funclist.get(choice, "invalid()"))
	
	# end of main

if (__name__ == "__main__"):
	main()
