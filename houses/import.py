#! python3
# Author: JGSnyder
# Date: 14 June 2020
# Imports csv to database

import csv
import sys
import sqlite3
import pandas as pd

# Check for one command line argument
if len(sys.argv) != 2:
    sys.exit("One command line argument accepted.")

# Check if file is csv
if not sys.argv[1].endswith(".csv"):
    sys.exit("Import csv file.")

with open(sys.argv[1], "r") as file:
    # Open csv file
    reader = csv.DictReader(file)
    # Connect to DB using sqlite3
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    for row in reader:
        splitName = row["name"].split()
        if len(splitName) == 3:
            row["first"] = splitName[0]
            row["middle"] = splitName[1]
            row["last"] = splitName[2]
        else:
            row["first"] = splitName[0]
            row["middle"] = None
            row["last"] = splitName[1]
        c.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", (row["first"], row["middle"], row["last"], row["house"], row["birth"]))
        # Applies above commands to the database
        conn.commit()
    conn.close()