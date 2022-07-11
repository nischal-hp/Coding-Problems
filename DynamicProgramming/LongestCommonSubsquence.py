# (1143. Medium) Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# Solution 1 : Using 2D dp table. O(m*n) time and space.
# Let's take an example with ade and ae. The dp table can be represented in a 2D array as shown below :
#   a  e  
# a 1  2  0
# d 3  4  0
# e 5  6  0
#   0  0  0
# If we are taking a bottom up- approach. We first have to start with value 6, then go all the way upto value 1.
# At 1, if 2 characters are equal, then we have found 1 common subsequence, So we add 1 plus the value from the diagonal (which is 4)
# It means that if are finding the lcs in the rest of the 2 strings (e and de)

# At 1, if 2 characters are not equal, then we have to find the max out of the lcs of the 2 neighboring cells.
# One neighbor is got by removing a from str2 and the rest of str1. (That is e and ade)
# Another neighbor is got by removing a from str1 and the rest of str2. (That is ae and de)

# While starting from 6, we have to look at the diagonal. Hence, we need to append an extra 0, in both the rows and columns, to help with the base case.
# Final answer is the value at 1.

class Solution:
    # O(m*n) - Time and Space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]  # IMP : Add +1, to append the extra zeros
        
        for i in range(len(text1) -1,-1,-1):    # Strings have to traversed in the reverse order
            for j in range(len(text2) -1, -1, -1):
                if text1[i]==text2[j]:                    
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]

# Solution 2 : Same thing could be done the other way around. In that case, we return the last value
# Here, Zeros should be appended as the first row and column. So we can modify the 2 strings, to have an empty space at the front

class Solution:
    # O(m*n) - Time and Space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1= ' '+text1
        text2= ' '+text2
        dp = [[0 for j in range(len(text2))] for i in range(len(text1))]
        
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

# Solution 3 : Using recursion. Not very efficient. 
# Will cause TLE if cache is not used.
# Same as the above problem, we return dp(-1,-1) in this case as well.

class Solution:
    # Recursion Solution
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache       # IMP : To use this, otherwise will cause TLE
        def dp(i,j):
            if i<0 or j<0 or i>=len(text1) or j>=len(text2):
                return 0
            elif text1[i]==text2[j]:
                return 1+ dp(i-1,j-1)
            else:
                return max(dp(i,j-1),dp(i-1,j))
        return dp(len(text1)-1, len(text2)-1)