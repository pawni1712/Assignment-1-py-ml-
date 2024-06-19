#WAP a program that reads data from a CSV file and prints it to the console
#Let's do this in 3 ways

import csv
with open('Cruz.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            print(lines)
