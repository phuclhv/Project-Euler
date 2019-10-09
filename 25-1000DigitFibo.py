'''
https://www.projecteuler.net/problem=25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
'''
First approach:
Brute force
Time complexity: 0(n) with n is the number of digit.
Space complexity: 0(1)
'''
def indexNthDigitFibo(n):
  prev, curr, digit, idx = 1, 1, 0, 2
  while digit < n:
    curr = curr + prev
    prev = curr - prev
    if (curr / (10**digit) > 1):
      digit +=1
    idx +=1
  print(idx)

indexNthDigitFibo(1000)