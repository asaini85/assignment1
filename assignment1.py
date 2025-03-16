#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: Ajay Saini
Student ID: 1527130222

The python code in this file (assignment1.py) is original work written by
Ajay Saini. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    """Based on the algorithm by Tomohiko Sakamoto"""
    # We used Tomohiko Sakamoto's algorithm to determine the day of the week.
    # This algorithm calculates the day of the week for any given date.
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year"""
 
    # A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def mon_max(month: int, year: int) -> int:
    """Returns the maximum day for a given month. Includes leap year check"""
    
    # This function returns the number of days in a month, considering leap years for February.
    feb_max = 29 if leap_year(year) else 28
    mon_max_dict = {1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_max_dict[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582
    '''
    # We refactored this function to use leap_year and mon_max functions.
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1 # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year) # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def usage():
    """Print a usage message to the user"""
    # This function prints a usage message and exits the program.
    
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def valid_date(date: str) -> bool:
    """Check validity of date and return True if valid"""
    try:
        year, month, day = map(int, date.split('-'))
        print(f"Checking date: Year={year}, Month={month}, Day={day}")
        if len(date.split('-')[0]) != 4 or len(date.split('-')[1]) != 2 or len(date.split('-')[2]) != 2:
            print("Invalid date due to incorrect format.")
            return False
        if month < 1 or month > 12 or day < 1 or day > mon_max(month, year):
            print("Invalid date due to month or day range.")
            return False
        return True
    except ValueError:
        print("Invalid date due to ValueError.")
        return False

def day_count(start_date: str, stop_date: str) -> int:
    """Loops through range of dates, and returns number of weekend days"""
    # This function counts the number of weekend days between two dates.
    count = 0
    current_date = start_date
    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)
    return count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date, end_date = sys.argv[1], sys.argv[2]

    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekends = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")
