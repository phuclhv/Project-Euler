'''
https://www.projecteuler.net/problem=28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

'''
1st approach:
Use a little math trick behind it.
The sum would allways be 
1 +    3 + 5 + 7 + 9    +    13 + 17 + 21 + 25  +....
           2 range               4 range
Every 4 addition, the range between element will increase by 2
As size increase by 2, we add 4 more element in to the sum

'''
def sumSpiral(size):
  jump = 2
  currNum = 1
  spiralSum = 1
  for i in range(1,size,2):
    for _ in range(4):
      currNum += jump
      spiralSum += currNum
    jump += 2
  return spiralSum

print(sumSpiral(1001))

