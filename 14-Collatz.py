'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

def startCollatzNum(limit):
  collatzDict = {1:1}
  maxChain = 0
  maxChainValue = -1
  for i in range(limit+1, 1, -1):
    currSeq = []
    value = i
    while value not in collatzDict:
      currSeq.append(value)
      if (value % 2 == 0):
        value = value // 2
      else:
        value = value * 3 + 1
    for i in range(len(currSeq)):
      collatzDict[currSeq[i]] = collatzDict[value] + len(currSeq) - i
  
  for key, value in collatzDict.items():
    if value > maxChainValue :
      maxChainValue = value
      maxChain = key
  
  print(maxChainValue, maxChain)

startCollatzNum(1000000)
    