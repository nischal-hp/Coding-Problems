# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# Solution 1 : Brute Force O(n^2)
# Since it has to be a contiguous array. Iterate through array. For each element check the sum with every other element until end of array.
# Keep track of the maximum value and return it in the end.

# O(n^2) solution - Brute Force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=-float(inf)
        for i in range(len(nums)):
            localSum=nums[i]
            maxSum=max(maxSum,localSum)   # IMP : Check the maximum here as well. When we are at the last element. Just the single element could be maximum value
            for j in range(i+1,len(nums)): # IMP(contd.) : Or for an array with single element
                localSum+=nums[j]
                maxSum=max(maxSum,localSum)
        return maxSum

# Solution 2 : Time O(n) and Space O(n)
# Let's create another list that can store the maximum of total or nums[i]. Here total = (previous num + nums[i]).
# Then to find the maximum of all the sums, we'll have to traverse the list and return the maximum. This was O(n) time and O(n) space.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-float('inf')] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)

# Solution 3 : .Time : O(n) .Constant Space O(1)
# In above approach, we stored maximum total until nums[i] and then found the maximum subarray total in the end. We aren't doing anything good with the new list because in the end we are traversing the list to find the maximum total. 
# So, eliminate creating new list and instead use the original list itself to store the maximum value. This becomes O(n) time and O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)