"""
	li.nk : A new way to shorten
			your links.

	Author : @shardic1	
"""

# uses Python's SQLite3 library for
# custom link database
import sqlite3 as sql

# opens the default database file
def __init__():
	conn = sql.connect("links.db")

# message for invalid choice
def invalid():
	print("Invalid choice.")
	main()

# check availability of a link
def check():
	conn.execute()

def main():

	print("Welcome to li.nk (URL SHORTENER)!\n")
	print("| MENU |\n")
	print("1. Check availability of link")
	print("2. Avail link")
	print("3. Avail custom link")
	print("4. Remove link")
	print("5. Exit")

	choice = input("Enter choice: ")

	funclist = 
	{
		"1": "check()",
		"2": "avail()",
		"3": "avail_custom()",
		"4": "remove()",
		"5": "end()"
	}

	eval(funclist.get(choice, "invalid()"))
	
	# end of main

if(__name__ == "__main__"):
	main()