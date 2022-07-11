# (198. Medium) You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Solution 1 : O(n) Time and Space using an extra array

# Breaking the problem into smallest problem. If only one element is present, we return the first element.
# If there are 2 elements in the array, we return the max out of those two.
# If there are 3 elements, then we return whichever is the max of (current element+element which is 2 places behind it) or (prev element)
# The above is the subproblem using which we can build the dp array.

class Solution:
    # O(n) Time and Space using a DP array
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[-1]   # Max value will be at the last position
            
# Solution 2 : O(n) Time and O(1) space

# The above logic can be replicated using just 2 variables, without using an extra array to store the values.

class Solution:
    # O(n) Time and O(1) Space without using extra DP array
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev1,prev2= 0,0   # Two Previous Numbers, to the current position
        for i in range(len(nums)):
            tempMax = max(nums[i]+prev2,prev1)
            prev2=prev1
            prev1= tempMax
        return prev1   # Max value will be at the last position
            
        