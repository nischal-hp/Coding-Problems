# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Ex 1 :
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Ex 2 :
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Solution 1 : Using Extra variables to keep track of row and column numbers
# Can iterate over the entire matrix. When we encounter an element with 0 value, keep track of the 
# row and column number using extra two variables.
# Then make another pass over the matrix, and check if current row or column is present in the two variables.
# If so, set the value of it to be 0.

# Time : O(m*n)
# Space : O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m+n) space solution
        row = []
        column = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    row.append(i)
                    column.append(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0

# Solution 2 : Using First row and column of the matrix itself as a flag
# Challenge is to make space complexity as O(1).

# Rather than use additional variables like in prev soln, we can use matrix itself as an indicator.
# More specifically we can use the first row and column values as the indicators. 
# If we ecnounter any element in that row or column to be 0, then we set the first element of that row/column to 0.

# Imp thing to note is that matrix[0][0], is the first element for both row and column. 
# So to differentiate btw the two, we can use another boolean variable to indicate that first column has been set to 0;
# and matrix[0][0] can be used to indicate that first row has been set to 0.

# Algorithm : 

# 1. We iterate over the matrix and we mark the first cell of a row i and first cell of a column j, if the condition in the pseudo code above is satisfied. i.e. if cell[i][j] == 0.

# 2. The first cell of row and column for the first row and first column is the same i.e. cell[0][0]. Hence, we use an additional variable to tell us if the first column had been marked or not and the cell[0][0] would be used to tell the same for the first row.

# 3. Now, we iterate over the original matrix starting from second row and second column i.e. matrix[1][1] onwards. For every cell we check if the row r or column c had been marked earlier by checking the respective first row cell or first column cell. If any of them was marked, we set the value in the cell to 0. Note the first row and first column serve as the row_set and column_set that we used in the first approach.

# 4. We then check if cell[0][0] == 0, if this is the case, we mark the first row as zero.

# 5. And finally, we check if the first column was marked, we make all entries in it as zeros.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) space solution
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):   # IMP : Start from 1, because we have an extra variable to keep track of first column, which is is_col
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0