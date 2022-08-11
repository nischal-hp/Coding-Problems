# (3. Medium) Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# Solution 1 : O(n^2) time
# Iterating through each character, form all the substrings possible starting from that character.
# Keep a track of the longest substring without repeating char and return that.

# Solution 2 : Sliding Window, Two pointers - O(n) time. O(m) space, where m-length of longest substring without repeating char
# Have 2 pointers l,r. Initially l is at 0. Keep incrementing r until we find a repeating char.
# We can store all the char in substring inside a set.
# At this point, update l to be 1 more than previous. Also remove it from the set. Continue the process.

# NOTE : We have to keep repeating from the set, as long as we keep encountering the same character.

class Solution:
    # O(n) time, O(m) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l=0
        for r in range(len(s)):
            while s[r] in charSet:  # NOTE : Cannot use if condition here
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
