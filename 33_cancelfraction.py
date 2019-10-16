'''
https://www.projecteuler.net/problem=33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
import math
def denominator():
  def simplify_fraction(numerator, denominator):
    org_frac = numerator / denominator
    a, b, c, d = numerator//10, numerator %10, denominator // 10, denominator % 10
    if (c!= 0 and a == d and b/c == org_frac) or (d!=0 and b==c and a/d == org_frac):
      return True
    return False
  product_num = 1
  product_dem = 1
  for i in range(1,99):
    for j in range (i+1,99):
      if simplify_fraction(i,j):
        product_num *= i
        product_dem *= j
  
  for i in range(min(product_num, product_dem),1,-1):
    if product_dem % i == 0  and product_num % i == 0:
      print(product_dem // i)
      return

denominator()