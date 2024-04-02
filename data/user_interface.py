from datetime import date
from operator import attrgetter
import os
import time

from data.todays_name_day import show_todays_names
from data.holidays import Holidays
from data.date_validation import date_validation
from data.persistence import save_holidays


def main_screen():
    welcoming()
    # show_todays_names()
    show_next_holidays(Holidays.ALL_HOLIDAYS)
    menu()


def welcoming():
    print(f"Mamy dziś {date.today().strftime('%d.%m.%y')}")


def show_next_holidays(holidays_list):
    print(40*"-", "\nNajbliższe ważne daty to:")
    next_holidays = Holidays.next_holidays(holidays_list)
    for holiday in next_holidays:
        print(holiday)


def menu():
    print(40*"-", "\n"
          "(1)wyświetl wszystkie święta;\n"
          "(2)dodaj osobę;\n"
          "(X)wyjdź;")
    option = input()
    if option == "1":
        show_all_holidays()
        input("\nDowolny klawisz, aby kontynuować.")
        main_screen()
    elif option == "2":
        person_name = input("Podaj osobę: ")
        add_person(person_name)
    elif option.lower() == "x":
        return
    else:
        print("Nieznana komenda.")
        os.system("cls")
        main_screen()


def show_all_holidays():
    for holiday in sorted(Holidays.ALL_HOLIDAYS, key=attrgetter("person_name", "day_type")):
        print(holiday)


def person_is_not_new(name):
    for holiday in Holidays.ALL_HOLIDAYS:
        if name == holiday.person_name:
            return True


def add_person(name):
    if person_is_not_new(name):
        print("Taka osoba już jest w bazie danych.")
        time.sleep(3)
        main_screen()
    else:
        str_date = input("Data urodzin dd.mm: ")
        list_date = date_validation(str_date)
        new_holiday = Holidays(name, Holidays.BIRTHDAY, list_date[0], list_date[1])
        Holidays.ALL_HOLIDAYS.append(new_holiday)
        str_date = input("Data imienin dd.mm: ")
        list_date = date_validation(str_date)
        new_holiday = Holidays(name, Holidays.NAME_DAY, list_date[0], list_date[1])
        Holidays.ALL_HOLIDAYS.append(new_holiday)
        additional_holidays = input("Dodatkowe święta? (T)Tak; (N)Nie ")
        if additional_holidays.lower() == "t":
            holiday_type = input("Podaj rodzaj święta: ")
            str_date = input("Data święta dd.mm: ")
            list_date = date_validation(str_date)
            new_holiday = Holidays(name, holiday_type, list_date[0], list_date[1])
            Holidays.ALL_HOLIDAYS.append(new_holiday)
        save_holidays(Holidays.ALL_HOLIDAYS)
        os.system("cls")
        main_screen()
