'''
Visualization with the 2D array index
       00 
    10    11
  20   21  22
 30  31  32  33
40  41  42  43  44

Dynamic Programming Approach:
We can see that as we go from the bottom to the top, we can choose to the highest value to be optimal
maxValue is the 2D array to hold that purpose, the formula is
maxValue[row][col] = max(maxValue[row+1][col], maxValue[row+1][col+1]) + grid[row][col]
'''
def path():
  f=open("./data/triangle.txt", "r")
  if f.mode == 'r':
    grid = [[int(number) for number in line.split(" ")] for line in f.readlines()]

  maxValue = [row[:] for row in grid]
 
  maxRow =  len(grid)
  maxCol = len(grid[maxRow-1])
  for col in range(maxCol):
    maxValue[maxRow-1][col] = grid[maxRow-1][col]

  for row in range(maxRow-2, -1, -1):
    for col in range(len(grid[row])):
      right = -float("inf")
      if (col + 1 < len(grid[row+1])):
        right = maxValue[row+1][col+1]
      left = maxValue[row+1][col]
      maxValue[row][col] = max(left, right) + grid[row][col]
  
  print(maxValue[0][0]) 
    
path()
