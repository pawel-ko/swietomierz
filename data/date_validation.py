MONTH_DAYS = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def date_validation(str_date):
    while not correct_date(str_date):
        print("Niepoprawna data. Spróbuj jeszcze raz.")
        str_date = input()
    return date_str_to_int_list(str_date)


def date_str_to_int_list(str_date):
    if "." in str_date:
        date_data = str_date.split(".")
    elif "," in str_date:
        date_data = str_date.split(",")
    else:
        raise ValueError("Nieprawidłowy format podanej daty.")

    try:
        date_data[0] = int(date_data[0])
        date_data[1] = int(date_data[1])
    except TypeError:
        raise TypeError("Nieprawidłowy format podanej daty.")

    return date_data


def correct_date(str_date):
    date_data = date_str_to_int_list(str_date)
    return 1 <= date_data[1] <= 12 and date_data[0] <= MONTH_DAYS[date_data[1]-1]
