#import pandas as pd
#import numpy as np
import csv
import itertools
import sys
from person import Person
from HeapManager import HeapManager
from schedule import Schedule

def main():
  sched = Schedule()
  personList = []
  file = sys.argv[1]
  with open(file) as csv_file:
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
      elif row[4] == 'Eboard':
        grade = 5
      else:
        grade = 0
      
      top5 = []
      for i in range(10, 17):
        if(row[i] != ""):
          top5.append((i-10, row[i][:4]))
          break
      for i in range(17, 24):
        if(row[i] != ""):
          top5.append((i-17, row[i][:4]))
          break
      for i in range(24, 31):
        if(row[i] != ""):
          top5.append((i-24, row[i][:4]))
          break
      for i in range(31, 38):
        if(row[i] != ""):
          top5.append((i-31, row[i][:4]))
          break
      for i in range(38, 45):
        if(row[i] != ""):
          top5.append((i-38, row[i][:4]))
          break
      
      possible = []
      for slot in range(45, 52):
        if(row[slot] != ""):
          can_do = row[slot].split(", ")
          #print(can_do)
          for item in can_do:
            possible.append((slot-45, item[:4]))
      #print(possible)

      impossible = []
      for slot in range(52, 59):
        if(row[slot] != ""):
          cant_do = row[slot].split(", ")
          #print(cant_do)
          for item in cant_do:
            impossible.append((slot-52, item[:4]))
      #print(impossible)

      dj = Person(row[2], float(row[9]), grade, top5, possible, impossible) 
      personList.append(dj)
      #0 is Monday, 6 is Sunday

  queue = HeapManager(personList)
  nonfinalized = []
  neglected = []
  pref = False
  nextDJ = queue.getNext()
  while(nextDJ != -1):
    for time in nextDJ.preferred_time:
      if(sched.isOpen(time[0], time[1])):
        sched.assignTime(time[0], time[1], nextDJ.name)
        nextDJ.scheduled = True
        pref = True
        break
    if(not pref):
      for time in nextDJ.other_time:
        if(sched.isOpen(time[0], time[1])):
          sched.assignTime(time[0], time[1], nextDJ.name)
          nonfinalized.append([time[0], time[1], nextDJ])
          nextDJ.scheduled = True
          pref = True
          break
    if(not pref):
      found = False
      for movableDJ in nonfinalized:
        for time in movableDJ[2].other_time:
          if((((time[0], time[1]) in nextDJ.other_time or time[0], time[1]) in nextDJ.preferred_time) and sched.isOpen(time[0], time[1])):
            sched.assignTime(time[0], time[1], movableDJ[2].name)
            sched.assignTime(movableDJ[0], movableDJ[1], nextDJ.name)
            movableDJ[0] = time[0]
            movableDJ[1] = time[1]
            nextDJ.scheduled = True
            found = True
            pref = True
            break
        if(pref):
          break
        if(not found):
          nonfinalized.remove(movableDJ)
    if(not pref):
      neglected.append(nextDJ)
      

    pref = False
    nextDJ = queue.getNext()

  sched.show()
  for dj in neglected:
    print(dj.name)


 
if __name__ == "__main__":
  main()
