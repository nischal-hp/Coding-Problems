# (212. Hard) Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# Solution 1 : Similar to Word Search Problem. (TLE)
# This looks similar to Word Search problem. Instead of finding just a single word, we have a list of words to find in the board.
# For each word, we scan the board for starting char and run dfs from there in all 4 directions. 
# However time complexity becomes, O(word*m*n*4^(m*n))
# Since we iterate board for every word, it is word*m*n. Then to run dfs in all 4 directions, an extra factor of 4^(m*n) is added.

# This will cause a TLE issue.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res=[]
        for word in words:
            if self.exist(board,word):
                res.append(word)
        return res
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

# Solution 2 : Using Trie and DFS. One factor in time complexity gets reduced, which is word.
# Thus time complexity is : O(m*n*4^(m*n))
# Firstly we insert all the words into a Trie.
# Next we do only one pass of the entire board, doing dfs in all 4 directions at each place.
# We start with an empty string, and go on building word adding each char by char.
# We continue with dfs only if a path exists in Trie, meaning we might have a word.
# If we find the end of word during the process, we add it to the result set.
# We also need a set to make sure we don't visit an already visited position.

# IMP : 
# Once we found a word, we can remove it from Trie. So that we don't have duplicate words matching.
# To do this, we need another variable in Trie called as refs. refs=0 initially and also once we have already found that word, its set to 0.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1     # Means a duplicate word case. We have already found the word
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)