import json

from data.holidays import Holidays


def load_holidays(file_name="holidays.json"):
    loaded_holidays = []
    try:
        with open(file_name, "r") as holidays_file:
            holidays_data = json.load(holidays_file).get("holidays", [])
    except FileNotFoundError:
        holidays_data = []
    for holiday in holidays_data:
        loaded_holidays.append(Holidays.from_json(
            holiday["person_name"],
            holiday["day_type"],
            holiday["day"],
            holiday["month"])
        )
    return loaded_holidays


def save_holidays(holidays_list, file_name="holidays.json"):
    holidays_data = [
        {
        "person_name": holiday.person_name,
        "day_type": holiday.day_type,
        "day": holiday.day,
        "month": holiday.month
        }
        for holiday in holidays_list
    ]

    with open(file_name, "w") as holidays_file:
        json.dump({"holidays": holidays_data}, holidays_file, indent=2)
