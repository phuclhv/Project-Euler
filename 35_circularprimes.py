'''
https://www.projecteuler.net/problem=35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from math import sqrt
from test import average_time_taken
def circular_primes(limit):
  primes = [2]

  def is_prime(num):
    divisor_limit = int(sqrt(num)) + 1
    for prime in primes:
      if prime > divisor_limit:
        return True
      if num % prime == 0:
        return False
    return True

  for i in range(3, limit):
    if is_prime(i):
      primes.append(i)

  count = 0

  for prime in primes:
    cur_prime_str = str(prime)
    num_digits = len(cur_prime_str)
    check = True
    for i in range(1,num_digits):
      rotation = ''
      for j in range(num_digits):
        rotation += cur_prime_str[(i+j) % num_digits]
      
      if int(rotation) not in primes:
        check = False
        break
    if check:
      count += 1

  return count

limit = 1000000
average_time_taken(circular_primes,limit)
    
    
  