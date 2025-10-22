#!/usr/bin/python3

import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
