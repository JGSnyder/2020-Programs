#! python3
#! textfilesearch.py - Searches a user-defined folder for text files and a user-defined searchterm
import os
import re

while True:
    try:
        filename = input("Please enter the directory you'd like to search within: ")
        os.chdir(filename)
        break
    except FileNotFoundError:
        print ("Please try again using the nomenclature /Users/username/directory")
        
extension = input("What file extension would you like to search for? Extension must begin with a period like .pdf or .txt. :   ")    
userinput = input("Enter your search terms: ")
regex = re.compile(userinput, re.I)

for textfile in os.listdir():
    if textfile.endswith(extension):
        with open(textfile) as opentext:
            str = opentext.read()
            answer = re.findall(regex, str)
            if answer != []:
                print(textfile.ljust(30), answer)
            else:
                print(textfile.ljust(30), "No results found.")
