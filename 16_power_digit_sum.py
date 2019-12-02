'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''
def numDigitPower(num, exponent):
  value = num**exponent
  sumDigit = 0
  while (value > 0):
    digit = value % 10
    #print(digit)
    sumDigit += digit
    value = value // 10
  print(sumDigit)

num = 2
exponent = 1000
numDigitPower(num, exponent)
    