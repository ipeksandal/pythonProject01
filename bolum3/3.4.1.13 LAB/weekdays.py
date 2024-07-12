class WeekDayError(Exception):
    pass

class Weeker:
    DAYS_IN_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.DAYS_IN_WEEK:
            raise WeekDayError("Invalid day. Please provide a valid day abbreviation (e.g., 'Mon').")
        self.day_index = self.DAYS_IN_WEEK.index(day)

    def __str__(self):
        return self.DAYS_IN_WEEK[self.day_index]

    def add_days(self, n):
        self.day_index = (self.day_index + n) % 7

    def subtract_days(self, n):
        self.day_index = (self.day_index - n) % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
