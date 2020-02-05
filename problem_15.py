"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

m = 21  # row
n = 21  # column

my_grid = [[1]*m for i in range(n)]

for i in range(1, n):
    for j in range(1, m):
        my_grid[i][j] = my_grid[i-1][j] + my_grid[i][j-1]

result = my_grid[-1][-1]
print(result)

