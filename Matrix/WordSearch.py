# (79. Medium) Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Ex 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Ex 2 :
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

# Solution 1 : DFS Time : O(m*n*4^(len(word))), Space : O(m*n)
# Time is 4 times the len(word), because we call dfs on all the 4 sides and the max we can get to is the length of word.
# Once we find the starting char of word, call dfs from that position.
# In dfs function, if the index of the word is equal to the lenght of word, that means we have found the entire word, hence can return True.
# Return False for out of bound conditions. Also if char doesn't match the required value and also if we have already traversed that position.
# Hence, need to maintain a set, to make sure, that we don't go on the same path again.
# Make sure to remove the values from path set, before it is returned. By the end of it, would be left with an empty set
class Solution: 
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    if dfs(r, c, 0): return True
        return False
            
