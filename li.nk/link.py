"""
	li.nk : A new way to shorten
			your links.

	Author : @MPL0Y	
"""

# uses Python's SQLite3 library for
# custom link database
import sqlite3 as sql
import random

# connects the li.nk database
conn = sql.connect("links.db")

# message for invalid choice
def invalid():
	print("Invalid choice.\n")
	main()

def has_key(s):
	global conn
	# an efficient method to check key presence
	rows = conn.execute(f"""SELECT *
													FROM links
													WHERE key = \"{s}\"""")
	exists = False
	for r in rows:
		exists = True
		break
	return exists

# check availability of a link
def check():
	global conn
	key = input("Enter a key to check: li.nk/")
	if(has_key(key)):
		print(f"li.nk/{key} is not available.\n")
	else:
		print(f"li.nk/{key} is available.\n")

def avail():
	global conn
	url = input("Enter your URL: ")
	# generating random key for user
	# through an adjective+verb combination
	nouns = open("nouns.txt", "r")
	adjectives = open("adjectives.txt", "r")
	noun = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in nouns])
	adjective = random.choice([i.rstrip().rstrip("\n").lstrip().lstrip("\n") for i in adjectives])
	key = adjective + noun
	conn.execute(f"""INSERT INTO links (key, url)
									VALUES ({key}, {url});""")
	conn.commit()
	print("Your personal link is created!")
	print(f"{url} is now: li.nk/{key}")

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

if(__name__ == "__main__"):
	main()