import math
def sum_truncated_primes():
  def is_prime(num):
    limit = int(math.sqrt(num))
    if num % 2 == 0:
      return False
    for i in range(3, limit,2):
      if num % i == 0:
        return False
    return True

  
eligible_digits = ('1','2', '3', '5', '7', '9')
truncate_primes = set()
while len(truncate_primes) < 9:
  for digit  
  
  
