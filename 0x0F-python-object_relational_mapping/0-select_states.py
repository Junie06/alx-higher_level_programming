#!/usr/bin/python3

'''List states from a database'''

import MySQLdb
from MySQLdb.connector import connect

if __name__ = "__main__":
    with connect(user=argv[1], passwd=argv[2], db=argv[3],) as connection:
        states = "SELECT * FROM states"
        with connection.cursor() as cursor:
            cursor.execute(states)
            rows = cursor.fetchall()

            for row in rows:
                print(row)

