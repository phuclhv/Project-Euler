'''
https://www.projecteuler.net/problem=19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def countSunday(sYear, eYear):
  numSuns, dow = 0, 2
  months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  for i in range(sYear,eYear+1):
    months[1] = 28 + ((i % 4 == 0 and i % 100 !=0) or (i % 400 ==0))

    for month in months:
      dow += month % 7
      if (dow % 7 == 0):
        numSuns +=1
  print(numSuns)
  
countSunday(1901, 2000)
  


