'''
https://www.projecteuler.net/problem=15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
target_row = 20
target_col = 20
num_way = 0

'''
First Approach:
Recursion to find the way
Not working with 20x20 grid
'''

def findPath(x, y):
  global num_way, target_row, target_col
  if x == target_row and y == target_col:
    num_way +=1
  else:
    if x < target_row:
      findPath(x+1,y)
    if y < target_col:
      findPath(x,y+1)

'''
Second approach:
Dynamic programming.
Realize that to way to reach grid[i][j] = ways to reach grid[i-1][j] + ways to reach grid[i][j-1]
Initialze the first row and the first collum = 1
'''
def gridPath():
  global target_row, target_col
  grid = [[0] * (target_row+1) for x in range(target_col+1)]
  for i in range(target_row+1):
    grid[i][0] = 1
  for j in range(target_col+1):
    grid[0][j] = 1
  
  for row in range(1, target_row+1):
    for col in range(1, target_col+1):
      grid[row][col] = grid[row-1][col] + grid[row][col-1]
  print(grid[target_row][target_col])

#findPath(0,0)
gridPath()
#print(numWays)