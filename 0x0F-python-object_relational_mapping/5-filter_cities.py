#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state = sys.argv[4]

        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")

        cursor = db.cursor()

        sql = "SELECT cities.name FROM states \
               INNER JOIN cities ON states.id = cities.state_id \
               WHERE states.name = %s \
               ORDER BY cities.id ASC"

        cursor.execute(sql, (state,))

        results = cursor.fetchall()

        print(", ".join([row[0] for row in results]))

        cursor.close()
        db.close()
    else:
        print("Usage: {} username password database state".format(sys.argv[0]))
