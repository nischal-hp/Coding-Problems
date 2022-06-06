# Given an m x n matrix, return all elements of the matrix in spiral order.

# Ex 1 :
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Ex 2 :
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Solution : Four Pointer Solution
# We need to have 4 pointers: left,right,top,bottom to indicate the boundaries of the matrix.
# We start from top left element and go all the way to bottom right.
# Since we are done with top row, we can increment the variable now.
# Next we go from top right to bottom right.
# IMP : Check if we have already found the breaking condition, since we updated the 2 variables in the above step.

# THen from bottom right to bottom left.
# Finally bottom left to top left.
# Increment variables at each step appropriately.
# Repeat the process until we have found the breaking condition
# Reference : https://www.youtube.com/watch?v=BJnMZNwUk1M&ab_channel=NeetCode

# Time : O(m*n), Space: O(1), if we dont consider the output array

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output=[]
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        # Repeat until the condition is satisfied
        while left<right and top<bottom:
            # Iterate through first row
            for i in range(left,right):
                output.append(matrix[top][i])
            top+=1
            # Iterate through last column
            for i in range(top,bottom):
                output.append(matrix[i][right-1])
            right-=1
            # IMP condition to be added : To make sure that we havent already found the breaking condition
            if not(left<right and top<bottom):
                break
            # Iterate through last row in reverse order
            for i in range(right-1,left-1,-1):
                output.append(matrix[bottom-1][i])
            bottom-=1
            # Iterate through first column in reverse order
            for i in range(bottom-1,top-1,-1):
                output.append(matrix[i][left])
            left+=1
        return output
        