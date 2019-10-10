'''
https://www.projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
'''
First approach:
Use 2 math fact that
1) Lenght of repeating cycle in primes are larger than normal number
2) A prime x will have x-1 repeating cycle when ((10**x) % x == 1

--> Run from the top, to find the biggest prime to satisfy 2. 
'''

import math
import time
TEST_CYCLES = 10
def countCycle(limit):
  def checkPrimes(n):
    for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True

  maxRecurLen = 0
  res = 0
  for x in range (limit,1,-1):
    if x < maxRecurLen:
      break
    if checkPrimes(x):
      modulo = 1
      for recurLen in range (1,x):
        modulo = (modulo * 10) % x    # Mod x each time to keep modulo small
        if modulo == 1:               
          if maxRecurLen < recurLen:
            maxRecurLen = recurLen
            res = x
          break                       
  return res

def averageTimeTaken(target):
  sumTimeTaken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    countCycle(target)
    sumTimeTaken += time.process_time() - start
  return sumTimeTaken / float(TEST_CYCLES)

target = 1000
print(("Average time taken for {} is {} sec. Result: {}").format(target,averageTimeTaken(target),countCycle(target)))


target = 100000
print(("Average time taken for {} is {} sec. Result: {}").format(target,averageTimeTaken(target),countCycle(target)))

target = 10000000
print(("Average time taken for {} is {} sec. Result: {}").format(target,averageTimeTaken(target),countCycle(target)))

# Average time taken for 1000 is 0.0015625 sec. Result: 983
# Average time taken for 100000 is 0.01875 sec. Result: 99989
# Average time taken for 10000000 is 1.6609375 sec. Result: 9999943
