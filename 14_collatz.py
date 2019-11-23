'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

def start_collatz_num(limit):
  # save all the known collatz value so far
  # key: number
  # value: collatz number of the key
  collatz_chains = {1:1}

  maxChain = 0
  maxChainValue = -1

  for i in range(limit+1, 1, -1):
    # store the sequence starting with i
    curr_seq = []
    value = i
    # if it is not stored all ready, we must initiate the chain
    while value not in collatz_chains:
      curr_seq.append(value)
      if (value % 2 == 0):
        value = value // 2
      else:
        value = value * 3 + 1
    
    # Put all the value in curr_seq to the collatz
    for i in range(len(curr_seq)):
      collatz_chains[curr_seq[i]] = collatz_chains[value] + len(curr_seq) - i
  
  # get the max from all the value
  for key, value in collatz_chains.items():
    if value > maxChainValue :
      maxChainValue = value
      maxChain = key
  
  print(maxChainValue, maxChain)

start_collatz_num(13)
start_collatz_num(9999)
start_collatz_num(1000000)
    