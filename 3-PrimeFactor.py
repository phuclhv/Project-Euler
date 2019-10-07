
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
def primeFactor(value):
  primeArr = [2]
  while (value % 2 == 0):
    value = value / 2
    lastFactor = 2

  def checkPrime(num):
    for pastPrime in primeArr:
      if (num % pastPrime == 0):
        return False
    return True

  limitFactor = math.sqrt(value)
  factor = 3
  
  while value > 1 and factor < limitFactor:
    if checkPrime(factor):
      primeArr.append(factor)
      while (value % factor == 0):
        value = value // factor
        lastFactor = factor
    factor += 2
  return lastFactor

print(primeFactor(600851475143))
      
