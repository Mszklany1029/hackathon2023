#import pandas as pd
#import numpy as np
import csv
import itertools
from person import Person
from HeapManager import HeapManager

def main():
  personList = []
  with open('data/show request form sample - Form Responses 1.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)
    for row in reader:
      if row[9] == '':
        row[9] = 0

      if row[4] == 'Student':
        if row[5] == 'Freshman':
          grade = 1
        elif row[5] == 'Sophomore':
          grade = 2
        elif row[5] == 'Junior':
          grade = 3
        elif row[5] == "Senior":
          grade = 4
        elif row[5] == 'Graduate':
          grade = 3
      else:
        grade = 0
      test_list = [2330, 1900, 2030, 700, 830]
      othertest_list = [100, 300, 500, 1430, 1600]
      otherothertest_list = [1,2,3,4,5,6]
      dj = Person(row[2], float(row[9]), grade, test_list, othertest_list, otherothertest_list)
      personList.append(dj)

  queue = HeapManager(personList)
  nextDJ = queue.getNext()
  while(nextDJ != -1):
    print(nextDJ.name, nextDJ.hours, nextDJ.student)
    nextDJ = queue.getNext()
        #i, j = 10, 45
    #reader2 = csv.reader(csv_file)
    #for row in reader2:
      #print(row[4])
      #for column in itertools.islice(reader, i, j):
        #print(column)
      #print(row[2])
      #dj = Person(row[2], )


 
if __name__ == "__main__":
  main()
