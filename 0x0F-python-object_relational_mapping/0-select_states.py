#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
	mysql_username = sys.argv[1]
	mysql_password = sys.argv[2]
	database_name = sys.argv[3]

	db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

	cur = db.cursor()
	cur.execute('SELECT * FROM states')
	rows = cur.fetchall()
	for row in rows:
	  print(row)

	cur.close()
	db.close()
