'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

'''
First approach:
Brute force to find sum of all divisor of all number below limit
Save those into a dictionary called amicables
Go through every item in amicables to see if there are any matching items
Divide the result by 2 because we count twice for each match

Time complexity: O(n^3/2) (since we only go up to sqrt(n) for the divisor)
Space complexity: O(n) (for the dictionary)
'''

import math
def sumAmicable(limit):
  amicables = {}
  sumAmi = 0
  def sumDivisor(num):
    limit = int(math.sqrt(num))
    sumD = 1
    for i in range(2, limit+1):
      if (num % i == 0):
        sumD += i 
        if (i != num // i):
          sumD += num //i
    return sumD
    
  for i in range(2,limit):
    amicables[i] =  sumDivisor(i)

  for key, value in amicables.items():
    if value != key and value in amicables and amicables[value] == key:
      sumAmi += value + key

  print(sumAmi//2)

sumAmicable(10000)