#!/usr/bin/python3

"""script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, and is also safe from MySQL injections"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        exit(1)


    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()


    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,

    for row in cur.fetchall():
        print(row)


    cur.close()
    db.close()
