#! python3
# Author: JGSnyder
# Date: 14 June 2020
# Prints out roster of students based on provided house name

import sys
import sqlite3
import pandas as pd
from pandas import DataFrame

# Connect to database
conn = sqlite3.connect("students.db")
c = conn.cursor()
# SQL Query for distinct houses in students database
sql_query_house = "SELECT house FROM students;"
c.execute(sql_query_house)
distinct_house = c.fetchall()
# Returns list of distinct houses
distinct_house = ([tup[0] for tup in distinct_house])

# Force user to enter one command-line argument
if len(sys.argv) != 2 or sys.argv[1] not in distinct_house:
    sys.exit("Enter one command-line argument with the name of the house.")

# SQL Query to search student roster in house
sql_query_roster = "SELECT first, middle, last, birth FROM students WHERE house = '" + sys.argv[1] + "' ORDER BY last, first;"
for row in c.execute(sql_query_roster):
    if row[1] == None:
        print(' '.join((row[0], row[2] + ",", "born", str(row[3]))))
    else:
        print(' '.join((row[0], row[1], row[2] + ",", "born", str(row[3]))))
# Close database connection
conn.close()