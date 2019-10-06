import math
def productTriplet(sumABC):
  a = 1
  while a < sumABC/3:
    b = a + 1
    c = 1000 - a - b 
    dif = c*c - a*a - b*b
    while c > b:
      if dif == 0:
        return(a*b*c)
      b +=1
      c = 1000 - a - b 
      dif = c*c - a*a - b*b
    a+=1
  return 0

print(productTriplet(1000))