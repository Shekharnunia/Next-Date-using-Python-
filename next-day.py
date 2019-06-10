import datetime
from dateutil.parser import parse

day = input('enter date in YYYY-MM-DD : ')

today = parse(day)
date = today.day
month = today.month
year = today.year

if year % 4 == 0:
    leap_year = True

elif year % 100 == 0:
    leap_year = False
elif year % 400 == 0:
    leap_year = True
else:
    leap_year = False

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


if date < month_length:
    date += 1
else:
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print(f'{year}-{month}-{date}')
