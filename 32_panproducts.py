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
'''
from test import average_time_taken
def sum_pan_product():

  def is_pan(a,b):
    c = a * b
    str_a, str_b,str_c = str(a),str(b),str(c)
    if len(str_a) + len(str_b) + len(str_c) != 9:
      return False
    product_str_sorted = ''.join(sorted(str_a + str_b + str_c))
    if product_str_sorted == "123456789":
      return True
    return  False
  
  res = 0
  pan_set = set()
  for i in range(2,1000):
    for j in range(100,5000):
      if j < i:
        continue
      if is_pan(i,j) and i*j not in pan_set:
        pan_set.add(i*j)
        res += (i*j)
  
  return res

average_time_taken(sum_pan_product)
#Average time taken for None is 3.6359375s. Result: 45228