'''
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

''' 
First apprach: Brute force
Read everything to an array, sort it
Go through each words, caculate the score, add to sum

Time Complexity: O(n * m) with n is the number of words and m is the length of the longest words. Will be O(n log n) if log n > m.
Space Complexity: O(n) (for the array)
'''
ASCII_A = 64
def nameScore():
  f=open("./data/22-names.txt", "r")
  if f.mode == 'r':
    words = [x for x in f.read().replace('"','').split(',')]
  
  words.sort()
  sumScore, idx = 0, 1
  for word in words:
    scoreWord = 0
    for char in word:
      scoreWord += ord(char) - ASCII_A
    scoreWord *= idx
    sumScore += scoreWord
    idx +=1 
  print(sumScore)
  
nameScore()
