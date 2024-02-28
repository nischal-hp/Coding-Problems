# (200. Medium) Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'

# Solution 1 : O(m*n) time and space
# We can sink the island by setting 1 to 0, so that we don't end up visiting the already visited island.
# This solution modifies the original array, but does not use any additional space like in Solution 2, which uses a set to maintain the already visited element.
class Solution:
    # O(m*n) solution
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        count=0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
                return
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count

# Solution 2 : O(m*n) time and space
# This problem is very similar to PacificAtlanticWaterFlow problem. Similar approach is followed here.
# A single hash set is enough here, to mark the visited cells.

class Solution:
    # O(m*n) solution
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        visited= set()
        noOfIslands=0
        
        def dfs(r,c):
            if (r,c) in visited or r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0":
                return
            visited.add((r,c))
            grid[r][c]="0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    noOfIslands+=1
                    dfs(r,c)
        return noOfIslands