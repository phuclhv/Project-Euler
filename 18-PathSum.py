'''
    00 
  10 11
 20 21 22
30 31 32 33
'''

def path():
  f=open("./data/18-Pathsum.txt", "r")
  if f.mode == 'r':
    grid = [[int(number) for number in line.split(" ")] for line in f.readlines()]

  
  size = len(grid)
  #print(len(grid), len(grid[0]))
  maxPathValue = -float('inf')
  ways = 0
  #print(grid)
  def findWay(row, col,value):
    nonlocal maxPathValue, ways
    #print(row,col)
    #print(row, col, value)
    if row == len(grid) -1:
      #print(row,col)
      ways += 1
      if value + grid[row][col] > maxPathValue:
        maxPathValue = value + grid[row][col]
    else:
      if col > 0:
        findWay(row+1,col-1, value + grid[row][col])
      if col+1 < len(grid[row+1]):
        findWay(row+1,col+1, value + grid[row][col])
      findWay(row+1,col, value + grid[row][col])
  findWay(0,0,0)
  print(maxPathValue, ways)
    
path()
