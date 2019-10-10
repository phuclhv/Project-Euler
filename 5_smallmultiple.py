'''
Smallest multiple
https://www.projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
1st approach:
- Build prime array from 1->value
- Broke every number from 1->value into prime_factor. Remember the max power for each prime Factor. Saved it in an dictionary
- Use the dictionary to construct the final value
'''
import math
from test import average_time_taken,average_time_taken_no_result
def smallest_mutiple(value):
  primes = []
  prime_factor = {}

  def is_prime(num):
    for prime in primes:
      if (num % prime == 0):
        return False
    return True
  
  def broken_to_prime_factor(num):
    idx = 0
    curr_prime_factorr = {}
    
    while (num !=1):
      while (num % primes[idx] == 0 ):
        if primes[idx] in curr_prime_factorr:
          curr_prime_factorr[primes[idx]] +=1
        else:
          curr_prime_factorr[primes[idx]] =1
        num = num / primes[idx]
      idx +=1

    for key, value in curr_prime_factorr.items():
      if key not in prime_factor:
        prime_factor[key] = value
      else:
        prime_factor[key] = max(value, prime_factor[key])
  
  for i in range(2,value):
      if is_prime(i):
        primes.append(i)
        prime_factor[i] = 0
      broken_to_prime_factor(i)

  res = 1
  for value,occurence in prime_factor.items():
    res = res * (value**occurence)
  return res

''' 
2nd approach:
- Build the prime array
- Use math to shorten the time
'''

def smallest_mutiple_math(value):
  primes = []
  prime_factor = {}

  def is_prime(num):
    for prime in primes:
      if (num % prime == 0):
        return False
    return True
  
  def broken_to_prime_factor(num):
    idx = 0
    curr_prime_factorr = {}
    
    while (num !=1):
      while (num % primes[idx] == 0 ):
        if primes[idx] in curr_prime_factorr:
          curr_prime_factorr[primes[idx]] +=1
        else:
          curr_prime_factorr[primes[idx]] =1
        num = num / primes[idx]
      idx +=1

    for key, value in curr_prime_factorr.items():
      if key not in prime_factor:
        prime_factor[key] = value
      else:
        prime_factor[key] = max(value, prime_factor[key])
  
  for i in range(2,value):
      if is_prime(i):
        primes.append(i)
        prime_factor[i] = 0
      broken_to_prime_factor(i)

  res = 1
  for value,occurence in prime_factor.items():
    res = res * (value**occurence)
  return res

limit = 20
print("Test 1")
print("1st approach")
average_time_taken(smallest_mutiple,limit)
print("2nd approach")
average_time_taken(smallest_mutiple_math,limit)

print("\nTest 2")
limit = 10000
print("1st approach")
average_time_taken_no_result(smallest_mutiple,limit)
print("2nd approach")
average_time_taken_no_result(smallest_mutiple_math,limit)