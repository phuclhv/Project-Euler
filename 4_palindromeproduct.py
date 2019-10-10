'''
Largest palindrome product
https://www.projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
'''
1st approach:
Brute force from top down
'''
from test import average_time_taken
def largest_palindrome(limit):
  max_palindrome = 0
  for i in range(limit, 100, -1):
    for j in range (i, 100, -1):
      product = i * j 
      if product > max_palindrome and str(product) == str(product)[::-1]:
        max_palindrome = product
  return max_palindrome

limit = 999
average_time_taken(largest_palindrome,limit)
# Average time taken for 999 is 0.028125s. Result: 906609

