'''
https://www.projecteuler.net/problem=1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
Solutions:

First method: Go through every number <  target, check if it divisible by 3 or 5 then add it

Second method: Find all divisible by 3 that is less target, do the same with 5, then 15, 
The result will be sum_divisible_by(target,3) + sum_divisible_by(target,5) - sum_divisible_by(target,15)
'''

import time
TEST_CYCLES = 10
def sum_multiples(max_num):
  res = 0
  for num in range(max_num):
    if num % 3 == 0 or num % 5 == 0:
      res += num
  return res

def sum_divisible_by(max_num, divisor):
  res, curr_num = 0, divisor
  while curr_num <= max_num:
    res += curr_num
    curr_num += divisor
  return res

def average_time_taken_1st(target):
  sum_time_taken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    sum_multiples(target)
    sum_time_taken += time.process_time() - start
  return sum_time_taken / float(TEST_CYCLES)

def average_time_taken_2nd(target):
  sum_time_taken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    sum_divisible_by(target,3)
    sum_divisible_by(target,5)
    sum_divisible_by(target,15)
    sum_time_taken += time.process_time() - start
  return sum_time_taken / float(TEST_CYCLES)

def overall_test(target):
  print("Testing with target = ", target)
  print("First method")
  print("Value: ", sum_multiples(target))
  print("Average time Taken: ", average_time_taken_1st(target))
  print("Second method")
  print("Value: ", sum_divisible_by(target,3) + sum_divisible_by(target,5) - sum_divisible_by(target,15))
  print("Average time Taken: ", average_time_taken_1st(target))
  print("\n")


overall_test(1000)
overall_test(100000)
overall_test(10000000)

# Testing with target =  1000
# First method
# Value:  233168
# Average time Taken:  0.0
# Second method
# Value:  234168
# Average time Taken:  0.0


# Testing with target =  100000
# First method
# Value:  2333316668
# Average time Taken:  0.0171875
# Second method
# Value:  2333416668
# Average time Taken:  0.012499999999999997


# Testing with target =  10000000
# First method
# Value:  23333331666668
# Average time Taken:  1.4203125
# Second method
# Value:  23333341666668
# Average time Taken:  1.471875

