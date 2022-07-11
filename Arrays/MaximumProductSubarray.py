# (152. Medium) Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Solution : This problem is similar to Maximum Subarray. But we cant employ the same solution here, because product is different than sum.
# Product of 2 negative nos will yield a positive result, and could be the max value we expect. Ex: -1*-2=2, but -1+ -2 = -3

# Solution 1 : Brute Force O(n^2)
# Find out all possible subarrays. Find the product in each of them, and then return the max

# Solution 2 : O(n) time, O(1) space
# The trick is to keep track of the max and min product upto the previous point. 
# That way, at each point we can multiple with both max and min product upto that point and find out which is greater.

# Another tricky edge case to keep in mind, is if 0 appears in the middle of an array. 
# In this case, we have to reset the counters of max and min product back to 1, since its basically like starting from the first; and then continue on.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n), O(1) solution
        res=max(nums)   # IMP : Find out the max and assign it to res, to deal with foll edge case : [-1,0,-2] 
        curMax, curMin = 1,1
        for i in range(len(nums)):
            if nums[i]!=0:  # In below statement, both should be in same line. Otherwise have to use tmp variable to store the prev curMax, before calculating the curMin.
                curMax, curMin = max(curMax*nums[i],curMin*nums[i],nums[i]),min(curMax*nums[i],curMin*nums[i],nums[i])
            else:
                curMax, curMin = 1,1  # To deal with edge case of [-1,0,-2]. We again have to start afresh after encountering 0 within the array
                continue

            res=max(res,curMax)
        return res