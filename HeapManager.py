import heapq

class HeapManager:

    def __init__(self, people):
        self.people = people
        eboard = []
        priority_students = []
        priority_community = []
        students = []
        community = []
        for p in people:
            if(p.student == 5):
                heapq.heappush(eboard, (-p.hours, p))
            elif(p.student == 0):
                if(p.hours < 8):
                    heapq.heappush(community, (-p.hours, p))
                else:
                    heapq.heappush(priority_community, (-p.hours, p))
            else:
                if(p.hours < 8):
                    heapq.heappush(students, (-p.hours, -p.student, p))
                else:
                    heapq.heappush(priority_students, (-p.hours, -p.student, p))
    
    def getNext(self):
        if(len(self.eboard) > 0):
            return heapq.heappop(self.eboard[1])
        elif(len(self.priority_students) > 0):
            return heapq.heappop(self.priority_students[2])
        elif(len(self.priority_community) > 0):
            return heapq.heappop(self.priority_community[1])
        elif(len(self.students) > 0):
            return heapq.heappop(self.students[2])
        elif(len(self.community) > 0):
            return heapq.heappop(self.community[1])
        else:
            return -1