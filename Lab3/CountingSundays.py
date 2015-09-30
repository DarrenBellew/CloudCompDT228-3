'''import datetime

daytime.MINYEAR = 1901
daytime.MAXYEAR = 2000

print(daytime.MAXYEAR)'''
import calendar

count = 0

year = 1901
endYear = 2001
month = 12

for x in range (year, endYear):
  for y in range (1, month+1):
    if calendar.weekday(x,y,1) == calendar.SUNDAY:
      count = count+1

print("Count: " + str(count))

