#! python3
# Author: JGSnyder
# Date: 04 June 2020
# Identifies to whom a sequence of DNA likely belongs

import sys, csv, re

# Check for 2 command line arguments.
if len(sys.argv) != 3:
    sys.exit("missing command line argument")

# Open csv file and read contents into memory
with open(sys.argv[1], newline='') as dna_master:
    dna_master_reader = csv.DictReader(dna_master)

    # Append all rows to dna_master_dict
    dna_master_dict = []
    for row in dna_master_reader:
        dna_master_dict.append(row)

    # Get headers of csv file to get DNA STR names to test against
    dna_str = dna_master_reader.fieldnames[1:] #AGATC, AATG, TATC

# Open dna_sample text file and read contents into memory
with open(sys.argv[2], "r") as text:
    dna_sample_text = text.read()
    matches = []
    dna_count_dict = {}

    # Search for each dna_str within provided sample text
    for STR in dna_str:
        matches = re.findall(r"(?:" + STR + ")+", dna_sample_text)
        if matches:
            largest_str = len(max(matches)) // len(STR)
            dna_count_dict.update({str(STR): str(largest_str)})

# Print out individual's name if there is a match
for row in dna_master_dict:
    count = 0
    for STR in dna_str:

        # check if STR is in the individual's DNA pattern
        if STR not in dna_count_dict:
            break

        #check if the master database matches the individual's DNA pattern
        if row[STR] != dna_count_dict[STR]:
            break
        else:
            count += 1
            if count == len(dna_str):
                print(row["name"])
                sys.exit(0)

print("No match")
sys.exit(1)