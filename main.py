from data.user_interface import main_screen
from data.holidays import Holidays
from data.persistence import load_holidays


if __name__ == '__main__':
    Holidays.ALL_HOLIDAYS = load_holidays()
    main_screen()
