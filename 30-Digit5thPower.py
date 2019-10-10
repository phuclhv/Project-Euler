'''
https://www.projecteuler.net/problem=30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
'''
1st approach
Brute force with some math involve
As 9**5 * 6 = 354294 and 9**5 * 7 = 413343. The number must be less than 354294.
'''
def sumAllDigit5thPower():
  limit = 9**5 * 6
  
  def sumDigit5thPower(num):
    sumDigit = 0
    while num > 0:
      sumDigit += (num%10)**5
      num = num // 10
    return sumDigit

  res = 0
  for number in range(limit,2,-1):
    if sumDigit5thPower(number) == number:
      res += number

  print(res)

sumAllDigit5thPower()