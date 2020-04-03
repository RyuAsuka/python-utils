import sys
import time


weekday = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA']


def str_week(year, month, day):
    """
    Calculate a specific day is what day of a week.
    :param year: The year
    :param month: The month
    :param day: The day
    :return: The weekday of this date.
    """
    if month == 1 or month == 2:
        month += 12
        year -= 1
    a = ((day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) + 1) % 7
    return a


def is_leap_year(year):
    """
    Judge if one year is leap year.
    :param year: The year.
    :return: True if the year is a leap year, else False
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def build_calendar(year, month):
    """
    Build the calendar of specific year and month.
    :param year: The year.
    :param month: The month.
    :return: The list of the calendar.
    """
    calendar = []
    title = [' SU', ' MO', ' TU', ' WE', ' TH', ' FR', ' SA']
    if month == 2 and is_leap_year(year):
        days = 29
    elif month == 2 and not is_leap_year(year):
        days = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    calendar.append(title)
    week = ['   ', '   ', '   ', '   ', '   ', '   ', '   ']
    for d in range(1, days+1):
        if str_week(year, month, d) == 0:
            if d != 1:
                calendar.append(week)
                week = ['   ', '   ', '   ', '   ', '   ', '   ', '   ']
        if 1 <= d < 10:
            week[str_week(year, month, d)] = '  %d' % d
        else:
            week[str_week(year, month, d)] = ' %d' % d
        if d == days:
            n = str_week(year, month, d)
            week = week[:n+1]
            calendar.append(week)
    return calendar


def output_calendar(calendar):
    """
    Format the calendar and output.
    :param calendar: The calendar created by the function build_calendar.
    :return: None
    """
    for line in calendar:
        for d in line:
            print(d, end='')
        print()


def print_help():
    """
    Print the help message.
    :return: None
    """
    print('Usage:\n'
          '    python3 calendar.py [year month]\n'
          'Output the calendar of specific year and month.\n'
          'If the parameter is ignored, the default output is current year and month.\n'
          'Parameters:\n'
          '    year: a range from [1583, 2100]\n'
          '    month: a range from [1, 12]')


if __name__ == '__main__':
    current_time = time.localtime()
    default_year = current_time.tm_year
    default_month = current_time.tm_mon
    if len(sys.argv) == 1:
        calendar = build_calendar(default_year, default_month)
        print(' ------ %d.%d ------' % (default_year, default_month))
        output_calendar(calendar)
        print()
    elif len(sys.argv) == 2:
        print_help()
    elif len(sys.argv) == 3:
        year = int(sys.argv[1])
        if year < 1583 or year > 2100:
            print('Error: parameter "year" is out of range.')
            exit(1)
        month = int(sys.argv[2])
        if month < 1 or month > 12:
            print('Error: parameter "month" is out of range.')
            exit(2)
        calendar = build_calendar(int(sys.argv[1]), int(sys.argv[2]))
        print(' ------ %d.%d ------' % (int(sys.argv[1]), int(sys.argv[2])))
        output_calendar(calendar)
        print()
    else:
        print_help()
