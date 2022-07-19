# (647. Medium) Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Solution 1 : O(n^2) time. - Soln similar to Longest Palindromic Substring problem.
# The soln. to this problem is very similar to Longest Palindromic Substring problem.
# Repeat the same process. Starting from each char, expand outwards to find all the substrings possible from that position.
# Keep a track of the count and keep adding it everytime. 

class Solution:
    # O(n^2) time
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd case, like "aba"
            count+=self.helper(s, i, i)
            # even case, like "abba"
            count+=self.helper(s, i, i+1)
        return count
    def helper(self,s, l, r):
            tempCount = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tempCount+=1
                l -= 1; r += 1
            return tempCount