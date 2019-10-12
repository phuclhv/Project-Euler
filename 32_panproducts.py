'''
https://www.projecteuler.net/problem=32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
'''
1st Approach: Brute force with Math
Assume that a < b and a*b = product is pandigital
We have 2 * 5000 = 10000 > 9 total digits and 100 * 100 = 10000 > 9 total digits
Thus a and b would be limit in range (2,100) and (100,5000) respectively with a < b

More finetune would be when we relize there's only 2 case:
Case 1: a has 1 digit, b has 4 digit, c has 4 digit
Case 2: a has 2 digit, b has 3 digit, c has 4 digit
'''
from test import average_time_taken
def sum_pan_product():

  def is_pan(a,b):
    c = a * b
    str_a, str_b,str_c = str(a),str(b),str(c)
    if len(str_a) + len(str_b) + len(str_c) != 9:
      return False
    product_str_sorted = str_a + str_b + str_c
    unique_digit = set()
    for char in product_str_sorted:
      if char == '0' or char in unique_digit:
        return False
      unique_digit.add(char)
    return  True
  
  res = 0

  # Case 1
  pan_set = set()
  for i in range(2,10):
    for j in range(1000,5000):
      if is_pan(i,j) and i*j not in pan_set:
        pan_set.add(i*j)
        res += (i*j)
  
  # Case 2
  for i in range(10,100):
    for j in range(100,1000):
      if is_pan(i,j) and i*j not in pan_set:
        pan_set.add(i*j)
        res += (i*j)
  return res

average_time_taken(sum_pan_product)
#Average time taken is 0.0921875s. Result: 45228