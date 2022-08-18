# (338. Easy) Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 10^5
 
# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

# Solution 1 : Using NumberOf1Bits problem as reference. O(n*number of 1 bits in i) time
# Basically for each value of i, we need to count the number of 1 bits in that i. Hence we can use that soln as reference.
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.hammingWeight(i))
        return ans
        
    def hammingWeight(self, n: int) -> int:
        count =0
        while n:
            n = n & (n-1)
            count+=1
        return count

# Solution 2 : O(n) time
# The idea here is that the number of 1 bits in some num i is: 1 if the last digit of i (i % 1) is 1, plus the number of 1 bits in the other digits of i (ans[i>>1] or ans[i // 2]).
# Try it on one of the example, if its doubtful     
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i>>1] + (i & 1)
        return ans