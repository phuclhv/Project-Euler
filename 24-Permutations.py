'''
https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
First approach
Use math
We can see that after choosing first digit, we have 9! choice. So moving 1 number in first digit == moving 9! place in order
Using the same approach with other digit, we can know where our lexicographic order are. 

Complexity: O(n^2) with n being the number of digit(not the limit), so it's blazingly fast
Space: O(n) 
'''
import math

def permutation(limit):
  remain_permu = limit
  availNum = [0,1,2,3,4,5,6,7,8,9]
  num = 9
  idx = 1
  while num > 0:
    idx = 0
    while remain_permu > math.factorial(num):
      remain_permu -= math.factorial(num)
      idx +=1
    print("{}".format(availNum[idx]),end="")
    availNum.pop(idx)
    num-=1
  print(availNum[0])

permutation(1000000)