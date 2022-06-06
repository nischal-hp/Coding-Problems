# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Ex 1 :
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Ex 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# Solution 1 : Using a result array to store the values. And then modifying the matrix.
# Time : O(m+n), Space : O(m+n)
# Taking the easiest case of 2*2 matrix [[1,2],[3,4]] after rotation becomes [[3,1],[4,2]].
# Which means we have to first pick column 1, iterate from last row to first. And then repeat the process again.
# Append these values in an array. Use the result array later to modify the original array.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=columns=len(matrix)

        result=[0]*(rows*columns)   # This will be the result array which stores the elements in the proper order
        
        for i in range(columns):
            for j in range(rows-1,-1,-1):                
                result.append(matrix[j][i])
        k=0
        while k<len(result):
            for i in range(rows):
                for j in range(columns):
                    matrix[i][j]=result[k]
                    k+=1

# Solution 2 : Using Transpose (swap elements along the diagonal) and Reflect operations (reverse elements in each row)
# Without using extra array to store the values. Constant Space O(1)
# The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal, and then reverse it from left to right. These operations are called transpose and reflect in linear algebra.
# So a matrix like [[1,2],[3,4]] after transposition becomes [[1,3],[2,4]]. After reflection becomes [[3,1],[4,2]], which is nothing but rotation of 90 degrees.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):   # IMP: Only one swap to be done. So start from one element after the ith element
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):   # IMP : To get until the middle element in each row
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]  

# Solution 3 : Using Constant Space again. Rotate Groups of Four Cells at a time. 
# Taking a 2*2 matrix as example. 
# [[1,2],[3,4]]. In step 1, tmp = 3. 
# After step 2, matrix becomes [[1,2],[4,4]]. After step 3, matrix becomes [[1,2],[4,2]]
# After step 4, matrix becomes [[1,1],[4,2]]. After step 5, matrix becomes [[3,1],[4,2]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):   # IMP : Rows has to be sum of both quotient and remainder of n
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]   # 1
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]  # 2
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]  # 3
                matrix[j][n - 1 - i] = matrix[i][j]  # 4
                matrix[i][j] = tmp  # 5

        