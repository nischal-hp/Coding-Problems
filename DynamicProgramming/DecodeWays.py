# (91. Medium) A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# Solution 1 : Brute Force. Recursion Tree. O(2^n)
# At each char, we can pick the next 1 char, or the next 2 characters depending on whether they lie in the given range.
# Ex : For 112, initially, we can pick either 1 or 11.
# When we are at 1, we can pick either 1 or 12. The process continues.
# Since we can make 2 decisions, at every instant, time becomes O(2^n)

# Solution 2 : DP O(n) time and space. Bottom-up approach
# Problem Reduction: variation of n-th staircase with n = [1, 2] steps.

# Approach: We generate a bottom up DP table.

# The tricky part is handling the corner cases (e.g. s = "30").

# Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

# Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

# For example:
# s = "231"
# index 0: extra base offset. dp[0] = 1
# index 1: # of ways to parse "2" => dp[1] = 1
# index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
# index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

# Notes:
# (1): Handling s starting with '0'. Alternative: I would recommend treating as an error condition and immediately returning 0. It's easier to keep track and it's an optimization.
# (2) (3): Pay close attention to your comparators. For (1) you want 0 <, not 0 <= . For (2) you want 10 <=, not 10 <

def numDecodings(s): 
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[len(s)]

# Solution 3 : Constant space 
# Since at a time, we only make use of 2 prev values, we could use 2 variables to store that. And we dont need an entire array.
# Here have used dp array with 2 values as the variables.

class Solution:
    # O(1) space
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            temp = 0
            if 1 <= int(s[i]) <= 9:
                temp = dp[1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += dp[0]
            dp = [dp[1], temp]
        return dp[1]