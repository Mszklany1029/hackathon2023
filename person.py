class Person:
    def __init__(self, name, hours, student, preferred_time, other_time):
        self.name = name
        self.hours = hours
        self.student = student # 0 = community member, 1-4 = year in school, 5 = eboard
        self.preferred_availability = preferred_time # list in preference order
        self.other_availability = other_time # list in no order