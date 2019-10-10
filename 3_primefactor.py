'''
Largest prime factor
https://www.projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
from test import average_time_taken

def prime_factor(value):
  primes = [2]
  while (value % 2 == 0):
    value = value / 2
    last_factor = 2

  def checkPrime(num):
    for pastPrime in primes:
      if (num % pastPrime == 0):
        return False
    return True

  limitFactor = math.sqrt(value)
  factor = 3
  
  while value > 1 and factor < limitFactor:
    if checkPrime(factor):
      primes.append(factor)
      while (value % factor == 0):
        value = value // factor
        last_factor = factor
    factor += 2
  return last_factor

limit = 600851475143
average_time_taken(prime_factor,limit)

#Average time taken for 600851475143 is 0.0296875s. Result: 6857

      
