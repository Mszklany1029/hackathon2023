import csv

with open('data/show request form sample - Form Responses 1.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[2])