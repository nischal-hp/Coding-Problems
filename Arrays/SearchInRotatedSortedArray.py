# (33. Medium) There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4

# Solution 1 : O(n)
# Simplt iterate through the array and find if the target value is present

# Solution 2 : O(logn)
# Since the array is sorted and there are 3 pointers - l,r,m. m can be in either left sorted portion or right sorted portion.
# If m is in left sorted portion. Then, if target value is > m or if target value < l, then we need to check on the right side.
# Otherwise need to check on the left side.

# Similarly, if m is in right sorted portion. If target value is < m or if target value > r, then we need to check on the left side.
# Else, check on the right side.

class Solution:
    # O(logn) time
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1      
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            if nums[m]>=nums[l]: # We are in left sorted portion
                if target>nums[m] or target<nums[l]:  # Check on the right side of mid
                    l = m+1
                else:                                 # Check on the left side of mid
                    r = m-1
            else: # We are in right sorted portion
                if target<nums[m] or target>nums[r]:  # Check on the left side of mid
                    r = m-1
                else:                                 # Check on the right side of mid
                    l = m+1
        return -1
         
        