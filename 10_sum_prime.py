'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import math
def sumPrime(maxPrimeValue):
  primeArr = [2]
  def checkPrime(num):
    for i in range(len(primeArr)):
      if num % primeArr[i] == 0:
        return False
      if primeArr[i] >= math.sqrt(num):
        return True
    return True

  currNum = 3
  res = 2
  while currNum < maxPrimeValue:
    if checkPrime(currNum):
      primeArr.append(currNum)
      res += currNum
    currNum += 2

  return res

  
print(sumPrime(2000000))
