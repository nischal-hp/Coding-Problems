# Easy Problem - Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Solution 1 : Sort 2 arrays and compare
# Easiest soln would be to sort the 2 arrays and check if they are same.
# Time - O(nlogn)

# Solution 2 : Using a Dictionary
# Populate the dictionary with letters from first string and also the count of each of them
# Iterate through second string, and go on decrementing the count of characters from dictionary.
# If a character is not present in dictionary, return False
# Finally iterate through dictionary and check if any value !=0. Return False
# Finally return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1
        for i in t:
            if i in dictionary:
                dictionary[i]-=1
            else:
                return False
        for each in dictionary.values():
            if each!=0:
                return False
        return True
                
                
        