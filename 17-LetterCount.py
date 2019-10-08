'''


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
'''
one, two, three, four, five, six, seven, eight, nine, ten
eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty
twentyone
ninetynine
ninehundredandninetynine
onehundredandtwelve
thirty
forty
fifty
sixty
seventy
eighty
ninety
'''
HUNDRED = 7
AND = 3
ONETHOUSAND = 11
def letterCount(target):
  sumCount = ONETHOUSAND
  currNum = 1
  oneDigit = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
  twoDigit= {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
  while (currNum < target):
    currLetterCount = 0
    checkNum = currNum
    if (checkNum >= 100):
      firstDigit = checkNum // 100
      currLetterCount += oneDigit[firstDigit] + HUNDRED + AND
      if (checkNum % 100 == 0):
        currLetterCount -= AND
        checkNum = 0
      else:
        checkNum = checkNum % 100
    if checkNum >=20:
      secondDigit = checkNum // 10
      thirdDigit = checkNum % 10
      currLetterCount += twoDigit[secondDigit] + oneDigit[thirdDigit]
    else:
      currLetterCount += oneDigit[checkNum]
    sumCount += currLetterCount
    currNum += 1
  print(sumCount)

letterCount(1000)