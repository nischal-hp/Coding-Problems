# (208. Medium) A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

# Motivation to Implement Trie :
# This problem consists of only lowercase engish characters, which means at most it can be 26.
# If we were to use another data structure such as hashmap or list. Then if we have to check the words starting with say "ban",
# Then we will have to iterate through the entire list or hashmap. 
# Whereas in the case of Trie, there is a root node. The children can be at max 26. Thus we need to check these 26 characters,
# and then proceed from there if it exists. This brings down runtime complexity.

# Mainly to implement the startsWith() function, we go for Trie. Otherwise other data structures could be more useful.

# There are several other data structures, like balanced trees and hash tables, which give us the possibility to search for a word in a dataset of strings. Then why do we need trie? Although hash table has O(1) time complexity for looking for a key, it is not efficient in the following operations :
# Finding all keys with a common prefix.
# Enumerating a dataset of strings in lexicographical order.

# Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to O(n), where n is the number of keys inserted. Trie could use less space compared to Hash Table when storing many keys with the same prefix. In this case using trie has only O(m) time complexity, where m is the key length. Searching for a key in a balanced tree costs O(mlogn) time complexity.

# Solution : 
# To implement Trie, we need to first have a TrieNode. Each TrieNode has a hashmap which stores its childrens.
# It also has another boolean variable, which indicates whether the character is end of word or not.
# A dummy root node is initialized. Since problem states there can only be lowercase english characters, trie can have atmost 26 children.
# Each node afterwards also can have atmost 26 children.
# We go on inserting char by char, and create a tree like structure. 

# Inserting a Word to Trie : 
# Time complexity : O(m), where m is the key length.
# In each iteration of the algorithm, we either examine or create a node in the trie till we reach the end of the key. This takes only mm operations.
# Space complexity : O(m).
# In the worst case newly inserted key doesn't share a prefix with the the keys already inserted in the trie. We have to add m new nodes, which takes us O(m) space.

# Search for a Word in Trie / Search for word prefix :
# Time : O(m)
# Space : O(1)

class TrieNode:
    def __init__(self):                
        self.children = {}
        self.EndOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()        # Dummy root node
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()        # If it doesnt exist, create one. Key is char, value is the TrieNode
            curr = curr.children[ch]               # If it already exists just iterate through it
        curr.EndOfWord = True             # In the end, set the boolean for last char
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        if curr.EndOfWord==True:          # Make sure to check whether it's end of word or not
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True                   # Same as search function, but here we don't need to check the boolean to find if its end of word or not
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)