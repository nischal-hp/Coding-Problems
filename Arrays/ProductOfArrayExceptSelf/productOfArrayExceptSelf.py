# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Solution approach : 
# An interesting observation to be made in this problem
# Suppose array is [1,2,3,4]. 
# The left prefix array is [-,1,12,123], where 123 means = 1*2*3rd element and - means 1(initial start point). Left prefix array means, we 
# start with 1, and then go on multiplying with the prev elements until that point and store in the current location. 
# The right prefix array for the same is [234,34,4,-]. 
# On multiplying both the above 2 arrays, we get the product array : [234,134,124,123]; which is our desired result.

# Approach 1 : Time and Space : O(n)
# Have 2 different arrays storing left and right prefix products. Finally multiply the 2 arrays. 

# Approach 2 : Space : O(1). Modify the result array directly, while doing the second pass; so that extra array is not needed.
# As given in problem, result array does not count toward space complexity.

# First pass - Create Left prefix array
# Second pass - Create right prefix array
# Third pass, which can be combined with second - multiple the above 2 arrays

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n=len(nums)
        p=1                    # A temporary variable used to start the prefix array
        for i in range(0,n):
            result.append(p)    # First pass
            p=p*nums[i]    
        p=1
        for i in range(n-1,-1,-1):
            result[i] = result[i]*p    # Third pass
            p=p*nums[i]                # Second pass
        return result 