'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
First approach:
- Build prime array from 1->value
- Broke every number from 1->value into primeFactor. Remember the max power for each prime Factor. Saved it in an dictionary
- Use the dictionary to construct the final value
'''
import math
def smallestMultiples(value):
  primeArr = []
  primeFactor = {}

  def checkPrime(num):
    for pastPrime in primeArr:
      if (num % pastPrime == 0):
        return False
    return True
  
  def brokenToPrimeFactor(num):
    idx = 0
    currPrimeFactor = {}
    
    while (num !=1):
      while (num % primeArr[idx] == 0 ):
        if primeArr[idx] in currPrimeFactor:
          currPrimeFactor[primeArr[idx]] +=1
        else:
          currPrimeFactor[primeArr[idx]] =1
        num = num / primeArr[idx]
      idx +=1

    for key, value in currPrimeFactor.items():
      if key not in primeFactor:
        primeFactor[key] = value
      else:
        primeFactor[key] = max(value, primeFactor[key])
  
  for i in range(2,value):
      if checkPrime(i):
        primeArr.append(i)
        primeFactor[i] = 0
      brokenToPrimeFactor(i)

  res = 1
  for value,occurence in primeFactor.items():
    res = res * (value**occurence)
  return res

''' 
Second approach:
- Build the prime array
- Use math to shorten the time
'''

def smallestMultiplesMath(value):
  primeArr = []
  primeFactor = {}

  def checkPrime(num):
    for pastPrime in primeArr:
      if (num % pastPrime == 0):
        return False
    return True
  
  def brokenToPrimeFactor(num):
    idx = 0
    currPrimeFactor = {}
    
    while (num !=1):
      while (num % primeArr[idx] == 0 ):
        if primeArr[idx] in currPrimeFactor:
          currPrimeFactor[primeArr[idx]] +=1
        else:
          currPrimeFactor[primeArr[idx]] =1
        num = num / primeArr[idx]
      idx +=1

    for key, value in currPrimeFactor.items():
      if key not in primeFactor:
        primeFactor[key] = value
      else:
        primeFactor[key] = max(value, primeFactor[key])
  
  for i in range(2,value):
      if checkPrime(i):
        primeArr.append(i)
        primeFactor[i] = 0
      brokenToPrimeFactor(i)

  res = 1
  for value,occurence in primeFactor.items():
    res = res * (value**occurence)
  return res

print(smallestMultiples(20))