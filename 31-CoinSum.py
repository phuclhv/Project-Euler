'''
https://www.projecteuler.net/problem=31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

'''
First approach:
Dynamic programming

With every loop, we increase the combination to be the ways of exchanging @value with the coins up to @coinIdx
'''

def coinChange(coinValue, amount):
  combinations = [0] * (amount+1)
  combinations[0] = 1

  for coinIdx in range(len(coinValue)):
    for value in range(coinValue[coinIdx],amount+1):
      combinations[value] += combinations[value-coinValue[coinIdx]]
  
  print(combinations[amount])

coinValue = [1,2,5,10,20,50,100,200]
amount = 200
coinChange(coinValue, amount)

  