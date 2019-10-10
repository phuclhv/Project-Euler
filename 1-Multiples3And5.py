'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
Solutions:

First method: Go through every number <  target, check if it divisible by 3 or 5 then add it

Second method: Find all divisible by 3 that is less target, do the same with 5, then 15, 
The result will be sumDivisibleBy(target,3) + sumDivisibleBy(target,5) - sumDivisibleBy(target,15)
'''

import time
TEST_CYCLES = 10
def sumMul(maxNum):
  res = 0
  for num in range(maxNum):
    if num % 3 == 0 or num % 5 == 0:
      res += num
  return res

def sumDivisibleBy(maxNum, divisor):
  res, currNum = 0, divisor
  while currNum <= maxNum:
    res += currNum
    currNum += divisor
  return res

def averageTimeTaken1st(target):
  sumTimeTaken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    sumMul(target)
    sumTimeTaken += time.process_time() - start
  return sumTimeTaken / float(TEST_CYCLES)

def averageTimeTaken2st(target):
  sumTimeTaken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    tmp = sumDivisibleBy(target,3) + sumDivisibleBy(target,5) - sumDivisibleBy(target,15)
    sumTimeTaken += time.process_time() - start
  return sumTimeTaken / float(TEST_CYCLES)

def overalTest(target):
  print("Testing with target = ", target)
  print("First method")
  print("Value: ", sumMul(target))
  print("Average time Taken: ", averageTimeTaken1st(target))
  print("Second method")
  print("Value: ", sumDivisibleBy(target,3) + sumDivisibleBy(target,5) - sumDivisibleBy(target,15))
  print("Average time Taken: ", averageTimeTaken1st(target))
  print("\n")


overalTest(1000)
overalTest(100000)
overalTest(10000000)

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

