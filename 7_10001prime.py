'''
10001st prime
https://www.projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math
from test import average_time_taken

def prime_factor(limit):
  primes = [2]

  def is_prime(num):
    for i in range(len(primes)):
      if num % primes[i] == 0:
        return False
      if primes[i] >= math.sqrt(num):
        return True
    return True
  
  curr_checking_number = 3
  while len(primes) != limit:
    if is_prime(curr_checking_number):
      primes.append(curr_checking_number)
    curr_checking_number += 2
  
  return primes[limit-1]

limit = 10001
average_time_taken(prime_factor,limit)

limit = 50000
average_time_taken(prime_factor,limit)

#Average time taken for 10001 is 0.2078125s. Result: 104743
#Average time taken for 50000 is 2.14375s. Result: 611953  
