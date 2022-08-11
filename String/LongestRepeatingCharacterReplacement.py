# (424. Medium) You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
 

# Constraints:

# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# Solution 1 : Brute Force : O(n^2) time. O(26) space
# The first set is to form all possible set of substrings, which is gonna be O(n^2).
# That means start from each char, go on adding every char after that to form a substring.
# Then we need a dictionary which keeps the count of each char in that substring.
# To check if substring is valid or not : Length of substring - count of max occuring char in that substring <= K,
# This means that if only one char is diff than the maximum occuring char in that substring, and its <=K, we can make that substitution.

# Solution 2 : Sliding Window. O(26*n) time, O(26) space
# This builds on solution 1.
# Using 2 pointers - l , r. 
# 1. We start from first char. Go on incrementing only r and also populating the dictionary;
# until the condition is satisfied : Length of sliding window - count of max occuring char in that substring <= K
# 2. When the condition is not satisfied, then increment l, and also reduce the count of the corresponding char from the dictionary.
# 3. Result is the max of the sliding window length each time a valid substring is found.

class Solution:
    # O(26*n) time, O(26) space
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        return res

# Solution 3 : O(n) time. O(26) space. Slight optimization to above solution 
# The optimization in above code is in the while loop, where we scan for max of the values in the dictionary. 
# We dont need to do that everytime. Instead just use another variable called maxf.
# We should try maximizing maxf, so that we get longer substrings. Hence we can neglect updating the value if its lesser than the prev value.

class Solution:
    # O(n) time, O(26) space
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l=0
        maxf=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])
            
            while (r-l+1) - maxf > k:
                count[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        return res
        
