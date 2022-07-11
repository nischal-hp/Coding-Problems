# (213. Medium) You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# Solution 1 : Using House Robber 1 solution and list slicing. O(n) time and Space
# The problem is same as House Robber 1 problem, but we can't include both the first and the last house in the list.
# So we need to find the max value excluding the first element; and also excluding the last element. Then find the max between the two.

# IMP : But, if we use list slicing, it becomes O(n) space solution, since it creates copies of the original list.

class Solution:
    # O(n) Time, O(n) space
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))  
    def helper(self,nums):        # This function is same as the one used in House Robber 1 problem.
        prev1,prev2= 0,0   # Two Previous Numbers, to the current position
        for i in range(len(nums)):
            tempMax = max(nums[i]+prev2,prev1)
            prev2=prev1
            prev1= tempMax
        return prev1   # Max value will be at the last position

# Solution 2 : O(n) time, O(1) space
# The above problem of list slicing can be easily overcomed by passing indices to the function, rather than list copies.

class Solution:
    # O(n) Time, O(1) space
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums,1,len(nums)),self.helper(nums,0,len(nums)-1))
    def helper(self,nums,i,j):
        prev1,prev2= 0,0   # Two Previous Numbers, to the current position
        for i in range(i,j):
            tempMax = max(nums[i]+prev2,prev1)
            prev2=prev1
            prev1= tempMax
        return prev1   # Max value will be at the last position