'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
import math
def primeFactor(value):
  primeArr = [2]
  def checkPrime(num):
    for i in range(len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True
  
  currNum = 3
  while len(primeArr) != value:
    if checkPrime(currNum):
      primeArr.append(currNum)
    currNum += 2
  
  return primeArr[value-1]

print(primeFactor(10001))

  
