# (417. Medium) There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Ex 1 :
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
 

# Constraints:
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

# Solution 1 : Brute Force O(m*n)^2
# We can start at each position in the matrix. Perform dfs in all 4 directions from that position; and
# have it in the result list, if it can meet both pacific and atlantic oceans.
# But the time complexity would be very much if we do it this way.

# Solution 2 : O(m*n) time and space
# A clever approach, is to do the problem in reverse. We start adjacent to the 2 oceans, and then do dfs in all 4 directions from there,
# if it could reach that particular ocean. 
# We maintain 2 hash sets, one for pacific, and one for atlantic. Finally we have to return the elements which is in both the hashsets.

# IMP : Diff btw list and Hash set. Hash set can have only unique values inside it. The values are unordered, and they cannot be indexed.
# IMP : We can use bitwise & operator in the end, to return the intersection set. 
# Diff btw and, & : and examines both the sides, and returns true if both are true. & does bitwise operations.
# Ex : 
# a = 14
# b = 4
  
# print(b and a) # 14
# print(b & a) # 4

class Solution:
    # O(m*n) solution
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r,c, visit, prevHeight):
            if (r,c) in visit or r<0 or c<0 or r>=ROWS or c>=COLS or prevHeight>heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])  # Call dfs on all 4 neighbors
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for c in range(COLS):    # Iterate through first and last row
            dfs(0,c, pacific, heights[0][c])    # First row is adjacent to pacific
            dfs(ROWS -1,c, atlantic, heights[ROWS -1][c])
        
        for r in range(ROWS):    # Iterate through first and last column
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])  # Last column is adjacent to atlantic
        
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

# Or the final res can be returned this way as well : 
return list(pacific & atlantic)    
        
        