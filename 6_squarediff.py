'''
Sum square difference
https://www.projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from test import average_time_taken
'''
First approach: brute force
'''
def sum_square_diff(limit):
  res = 0
  for i in range(limit):
    for j in range(i+1,limit):
      res += 2 * (i+1) * (j+1)
  return res

'''
Second approach: math
'''
def sum_square_diff_math(limit):
  sum = (limit * (limit + 1)) / 2
  sum_square = (2 * limit + 1) * (limit + 1) * limit / 6
  return sum**2 - sum_square

limit = 100
print("Test with: {}".format (limit))
print("1st approach: ")
average_time_taken(sum_square_diff,limit)
print("2nd approach")
average_time_taken(sum_square_diff_math,limit)

limit = 1000
print("\nTest with: {}".format (limit))
print("1st approach: ")
average_time_taken(sum_square_diff,limit)
print("2nd approach: ")
average_time_taken(sum_square_diff_math,limit)

limit = 10000
print("\nTest with: {}".format (limit))
print("1st approach: ")
average_time_taken(sum_square_diff,limit)
print("2nd approach: ")
average_time_taken(sum_square_diff_math,limit)

# Test with: 100
# 1st approach:
# Average time taken for 100 is 0.0s. Result: 25164150
# 2nd approach
# Average time taken for 100 is 0.0s. Result: 25164150.0

# Test with: 1000
# 1st approach:
# Average time taken for 1000 is 0.0625s. Result: 250166416500
# 2nd approach:
# Average time taken for 1000 is 0.0s. Result: 250166416500.0

# Test with: 10000
# 1st approach:
# Average time taken for 10000 is 6.575s. Result: 2500166641665000
# 2nd approach:
# Average time taken for 10000 is 0.0s. Result: 2500166641665000.0