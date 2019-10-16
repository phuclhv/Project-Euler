'''
https://projecteuler.net/problem=36
Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from test import average_time_taken

def sum_double_palindrome(limit):
  sum_double = 0
  for i in range(limit, 0, -1):
    if str(i) == str(i)[::-1]:
      binary_form = bin(i)[2:]
      if binary_form == binary_form[::-1]:
        sum_double += i
  return sum_double
  
limit = 1000000
average_time_taken(sum_double_palindrome,limit)
# Average time taken for 1000000 is 0.384375s. Result: 872187
