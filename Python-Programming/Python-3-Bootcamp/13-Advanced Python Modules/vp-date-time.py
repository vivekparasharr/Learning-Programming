# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:20:31 2020

@author: vivek
"""

import datetime

# set a time, for example 1pm 20 minutes 1 second 20 microseconds
# hour, minute, second, microsecond
print(datetime.time(13,20,1,20)) # 13:20:01.000020

# set a date works in a similar way
# year, month, date
print(datetime.date(2000,1,31)) # 2000-01-31
print(datetime.date.today()) # 2020-09-19
print(datetime.date.today().ctime()) # Sat Sep 19 00:00:00 2020

# set a date-time works in a similar way
# datetime is an object within datetime package
# year, month, date, hour, minute, second, microsecond
print(datetime.datetime.now()) # 2020-09-19 12:02:04.209513

# we can replace current date time using replace parameter
dttm=datetime.datetime.now()
print(dttm) # 2020-09-19 12:04:43.362993
dttm=dttm.replace(year=2021, month=10)
print(dttm) # 2021-10-19 12:04:43.362993

# arithmetic can be performed on date object or datetime object
# date
d1 = datetime.date(2021,11,3)
d2 = datetime.date(2020,11,1)
print(d1-d2) # 367 days, 0:00:00

# datetime
dttm1 = datetime.datetime(2021,11,3, 22,0)
dttm2 = datetime.datetime(2020,11,1, 20,0)
print(dttm1-dttm2) # 367 days, 2:00:00 hours

