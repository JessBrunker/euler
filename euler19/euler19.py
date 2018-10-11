#!/usr/bin/python3

'''
You are given the following information:

    - 1 Jan 1900 was a Monday.
    - Thirty days has September,
      April, June and NOvember.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, but not 
      on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
'''

import time


start = time.time()

# check if a given year is a leap year given the above conditions
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


# return the number of days in a month given the year
def days_in_month(month, year):
    if month in [9, 4, 6, 11]:
        return 30
    elif month != 2:
        return 31
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28


# initial values
year = 1900 
month = 1 
day = 1


sunday_count = 0
month_days = days_in_month(month, year)
day += 6 # to put the index on Sunday

while year <= 2000:
    # loop until it's in the next month
    while day < month_days:
        day += 7
    month += 1
    # looped into next year
    if month == 13:
        month = 1
        year += 1
    # subtract out the previous month to get the current day
    day -= month_days
    month_days = days_in_month(month, year)
    # only start counting from 1901
    if year == 1900:
        continue
    if day == 1:
        sunday_count += 1

print(sunday_count)




end = time.time()
print('{}s'.format(end-start))
