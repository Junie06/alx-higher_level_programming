#!/usr/bin/python3
'''List states from a database'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3]) as connection:
        states = "SELECT * FROM states WHERE name = %s"
        with connection.cursor() as cursor:
            cursor.execute(states, (argv[4], ))
            rows = cursor.fetchall()

            for row in rows:
                print(row)
