import heapq
from person import Person

class HeapManager:

    def __init__(self, people):
        self.people = people
        self.eboard = []
        self.priority_students = []
        self.priority_community = []
        self.students = []
        self.community = []
        i = 0
        for p in people:
            if(p.student == 5):
                heapq.heappush(self.eboard, (-p.hours, i, p))
            elif(p.student == 0):
                if(p.hours < 8):
                    heapq.heappush(self.community, (-p.hours, i, p))
                else:
                    heapq.heappush(self.priority_community, (-p.hours, i, p))
            else:
                if(p.hours < 8):
                    heapq.heappush(self.students, (-p.hours, -p.student, i, p))
                else:
                    heapq.heappush(self.priority_students, (-p.hours, -p.student, i, p))
            i += 1
    
    def getNext(self):
        #print(len(self.priority_students), len(self.priority_community), len(self.students), len(self.community))
        if(len(self.eboard) > 0):
            return heapq.heappop(self.eboard)[2]
        elif(len(self.priority_students) > 0):
            return heapq.heappop(self.priority_students)[3]
        elif(len(self.priority_community) > 0):
            return heapq.heappop(self.priority_community)[2]
        elif(len(self.students) > 0):
            return heapq.heappop(self.students)[3]
        elif(len(self.community) > 0):
            return heapq.heappop(self.community)[2]
        else:
            return -1

