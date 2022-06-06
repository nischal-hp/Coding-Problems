# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

# Constraints : 
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution 1 : Using Dictionary:
# The intuition is after sorting each element in the list, it can be used as a key value for the Dictionary.
# If value already exists in Dictionary, append it. Otherwise add the unsorted element to the Dictionary as value.

# IMP: sorted(str), returns a list with sorted characters. Hence, to convert it back to string have to use ''.join()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:
            return [strs]    # We need to return an array of answer
        mainDict={}
        for each in strs: 
            key=''.join(sorted(each))     # IMP: Since, sorted() returns a list of sorted characters, to convert it back to string 
            if key not in mainDict:
                mainDict[key]=[each]
            else:
                mainDict[key]+=[each]
        return mainDict.values()

# Solution 2 : Without using sort 
# The trick is to use a tuple as a key to the Dictionary.
# Each tuple is of length 26, indicating the number of characters in each string from a-z.
# Since question states all are of lower case characters, we can use this approach.

class Counter:
    def __init__(self, s=None):
        self.array = [0] * 26
        if s:
            self.count(s)
            
    def to_tuple(self):
        return tuple(self.array)
    
    def count(self, s):
        for cha in s:
            self.array[ord(cha) - ord('a')] += 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            counter = Counter(s)
            key = counter.to_tuple()
            
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
                
        return d.values()
            
            
        