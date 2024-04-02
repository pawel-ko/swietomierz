from operator import attrgetter

from datetime import date


class Holidays:

    BIRTHDAY = "urodziny"
    NAME_DAY = "imieniny"
    OTHER = None

    ALL_HOLIDAYS = []

    def __init__(self, person_name, day_type, day, month):
        self.person_name = person_name
        self.day_type = day_type
        self.day = day
        self.month = month

    @property
    def days_number(self):
        today = date.today()
        holiday_day = date(today.year, self.month,  self.day)
        if holiday_day < today:
            holiday_day = holiday_day.replace(year=today.year + 1)
        time_to_birthday = abs(holiday_day - today)
        return time_to_birthday.days

    @staticmethod
    def from_json(person_name, day_type, day, month):
        return Holidays(person_name, day_type, day, month)

    @staticmethod
    def next_holidays(holidays_list):
        holidays_to_show = []
        for holiday in sorted(holidays_list, key=attrgetter("days_number")):
            if holiday.days_number <= 31 or len(holidays_to_show) <= 5:
                holidays_to_show.append(holiday)
        return holidays_to_show

    def __str__(self):
        return f"{self.person_name} {self.day_type}: {self.day}.{self.month}; zostało {self.days_number}dni"
