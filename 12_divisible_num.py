'''
he sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
def numMoreDivisor(maxNumDivisor):
  curTri = 3
  sumTri = 3

  def checkDivisor(num):
    numDivisor = 2
    limitFactor = math.sqrt(num)
    divisor = 2
    while divisor <= limitFactor:
      if (num % divisor == 0):
        numDivisor += 1
        if divisor != num/divisor:
          numDivisor += 1
      divisor += 1
    return numDivisor
  
  while checkDivisor(sumTri) <= maxNumDivisor:
    sumTri += curTri
    curTri += 1
  print(sumTri)

numMoreDivisor(500)