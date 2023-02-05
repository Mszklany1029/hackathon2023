from tabulate import tabulate

class Schedule:

    def __init__(self):

        self.mondayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "PA",
            "1730": "PA",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.tuesdayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "PA",
            "1730": "PA",
            "1900": "",
            "2030": "MTP",
            "2200": "",
            "2330": ""
        }

        self.wednesdayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "PA",
            "1730": "PA",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.thursdayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "PA",
            "1730": "PA",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.fridayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "PA",
            "1730": "PA",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.saturdayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "",
            "1730": "",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.sundayDict = {
            "0100": "",
            "0300": "",
            "0500": "",
            "0700": "",
            "0830": "",
            "1000": "",
            "1130": "",
            "1300": "",
            "1430": "",
            "1600": "",
            "1730": "",
            "1900": "",
            "2030": "",
            "2200": "",
            "2330": ""
        }

        self.schedule = [self.mondayDict, self.tuesdayDict, self.wednesdayDict, self.thursdayDict, self.fridayDict, self.saturdayDict, self.sundayDict]
        self.week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def isOpen(self, dayOfWeek, time):
        weekIndex = self.week.index(dayOfWeek)
        return self.schedule[weekIndex][time] == ""

    def show(self):
        print(tabulate(self.schedule, headers = "keys", tablefmt = "grid", showindex=self.week))