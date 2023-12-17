#!/usr/bin/python3
'''List states from a database'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3]) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """, (argv[4], ))
            print(", ".join(map(lambda x: x[0], cursor.fetchall())))
