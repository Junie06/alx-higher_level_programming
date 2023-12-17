#!/usr/bin/python3

'''List states from a database'''

import MySQLdb

if __name__ = "__main__":
    with MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],) as connection:
        states = "SELECT * FROM states"
        with connection.cursor() as cursor:
            cursor.execute(states)
            rows = cursor.fetchall()

            for row in rows:
                print(row)

