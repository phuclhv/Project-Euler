'''
https://www.projecteuler.net/problem=27
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''
'''
First approach
Brute force with lots of tricks used to reduce time
'''
import math
import time
TEST_CYCLES = 10
def coefficientsProduct(limitA, limitB):
  
  def checkPrime(n):
    if n < 2:
      return False
    for i in range(2, int(math.sqrt(n)+1)):
      if n % i == 0:
        return False
    return True
  
  def equation(n,a,b):
    return n**2 + a*n + b
  
  primesLessthanLimitB = []
  for i in range(2,limitB):
    if checkPrime(i):
      primesLessthanLimitB.append(i)
  
  maxConsValue = 0
  currA,idxB = limitA, len(primesLessthanLimitB)-1
  maxA, maxB = 1, 41

  while currA > -limitA:
    idxB = len(primesLessthanLimitB)-1
    
    while idxB > -1:
      currB = primesLessthanLimitB[idxB]
      if (currB + maxConsValue**2 < -maxConsValue*currA):
        break
      consValue = maxConsValue
      checkValid = True

      while consValue >=0:
        if not checkPrime(equation(consValue,currA,currB)):
          checkValid = False
          break
        consValue -= 1

      if checkValid:
        consValue = maxConsValue + 1

        while True:
          if not checkPrime(equation(consValue,currA,currB)):
            maxConsValue = consValue
            maxA, maxB = currA, currB
            break
          consValue+=1
      idxB -=1

    currA -=1
  return (maxA * maxB)

#print(coefficientsProduct(1000,1000))  

def averageTimeTaken(target):
  sumTimeTaken = 0
  for _ in range(TEST_CYCLES):
    start = time.process_time()
    coefficientsProduct(target, target)
    sumTimeTaken += time.process_time() - start
  return sumTimeTaken / float(TEST_CYCLES)

limit = 1000
print(("Average time taken for {} is {} sec. Result: {}").format(limit,averageTimeTaken(limit),coefficientsProduct(limit,limit)))

#Average time taken for 1000 is 0.778125 sec. Result: -59231