# (5. Medium) Given a string s, return the number of palindromic substrings in it.
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Solution 1 : Brute Force O(n^3)
# Check for every possible substring, whether it's a palindrome or not.
# Start from each char, go on adding each char after that, and check it.
# Repeat this starting from each char.
# Ex: For 'abc'. Start from a. Possible substrings : a,ab,abc. Check if any of them are palindromes
# Next start from b. Possible substrings : b, bc. Check if any of them are palindromes
# Finally return the max length substring.

# Time : Checking if a substring is palindrome, is O(n). To form all possible substrings, it is O(n^2).
# Hence, total becomes O(n^3)

# Solution 2 : Start from middle, and expand and check for palindrome O(n^2)
# One way of checking whether a string is palindrome is to start from either ends, and go on moving towards the center.
# The other way is to start from the middle, expand on either direction, and check if its palindrome. 
# This reduces time complex. to O(n^2), and is preferred here.

# Edge Case : Following this method, we might miss a palindromic substring of even length, like in example 2.
# Hence, we have to make special provision for that, like shown in code.

# Note : In below soln, list slicing - return s[l+1:r], is also O(n) operation, which can make time complex. to becomes O(n^3).
# The workaround is to have 2 variables, and make use of that, rather than slice it.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]    # The char starting after l and ending before r, is the actual palindrome. Hence take from l+1 to r-1

