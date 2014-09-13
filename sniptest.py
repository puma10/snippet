import csv

name = "spam"

with open("snippets.csv", "rU") as file:
    my_file = csv.reader(file)
    for row in my_file:
        if row[0] == name:
            print row[1]
