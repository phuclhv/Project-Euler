'''
https://www.projecteuler.net/problem=34
Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
'''
Math analysis:
7 * 9! = 2 540 160 --> all the number we have to find will be less than 2 540 160
Suppose there is a number larger than 2 540 160 satisfy the requirement 
--> Sum of all its digit factorial > 2 540 160 = 7 * 9! --> Impossible
8 * 9! = 2 903 040 --> for number that have more than 8 digit, the sum of its digit factorial will never reach its sum
'''
'''
Approach:
Brute force
'''
from test import average_time_taken
def sum_digit_factorial():
  factorials = [1]
  LIMIT = 2540160
  sum_all_num = 0
  # Build an array of factorials for later use. factorials[i] = i!
  for i in range(1,10):
    factorials.append(factorials[i-1] * i)

  def check_digit_factorial(num):
    curr_check_num = num
    sum_check_num = 0
    while curr_check_num > 0:
      sum_check_num += factorials[curr_check_num % 10]
      curr_check_num = curr_check_num // 10
    if sum_check_num == num:
      return True
    return False
  
  for num in range(3, LIMIT):
    if check_digit_factorial(num):    
      sum_all_num += num
  return sum_all_num

average_time_taken(sum_digit_factorial)
# Average time taken is 2.575s. Result: 40730