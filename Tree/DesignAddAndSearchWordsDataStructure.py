# (211. Medium) Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 3 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.

# Solution 1 : Brute Force 
# Just use an array to store all the words. And then iterate through it, to check if it exists or not.
# As the number of words increases, this process becomes cumbersome.

# Solution 2 : Using Trie approach
# The add function is similar to Trie(Prefix Tree).
# Modifications are needed in Search().
# In case we encounter a character == '.', then we need to check all of its chidrens.
# Thus we need to build an approach which is both recursive and iterative.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.EndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]                    # We need to check each char by char, using the index
                if c == ".":
                    for child in cur.children.values():   # Check all the children, if a '.' is encountered
                        if dfs(i + 1, child):   # Recursive Part
                            return True
                    return False              # If none of the recursive calls return True, means we haven't found the word
                else:
                    if c not in cur.children:   # Iterative Part
                        return False
                    cur = cur.children[c]
            return cur.EndOfWord

        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)