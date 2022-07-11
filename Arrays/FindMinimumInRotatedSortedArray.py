# (153. Medium) Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.
 
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# Solution 1 : O(n) approach 
# Just iterate through array and find the minimum out of all.

# Solution 2 : O(logn) approach - Binary Search approach
# We can make use of the sorted property to reduce runtime.
# Suppose the left most element is less than right most element, it means we have a sorted array. The left-most element could be our result - #1
# If middle element is >= left element, it means we have a sorted array on the left side; so we need to search on the right side. Hence update the left pointer - #2
# Else we need to search on left side, hence update the right pointer - #3
# Initially take the first element as result element arbitrarily. 
class Solution:
    # O(logn) approach
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1
        
        while l<=r:
            if nums[l]<nums[r]:
                res= min(nums[l],res)  # 1
                break
            
            m = (l+r)//2
            res = min(res,nums[m])
            
            if nums[m] >= nums[l]:   # 2
                l = m+1
            else:
                r = m-1         # 3
        return res

# Solution 3 : Same as before, but using pivot point which is the point where element starts to decrease
# 1. Find the mid element of the array.
# 2. If mid element > first element of array this means that we need to look for the inflection point on the right of mid.
# 3. If mid element < first element of array this that we need to look for the inflection point on the left of mid.
# 4. We stop our search when we find the inflection point, when either of the two conditions is satisfied:
# nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
# nums[mid - 1] > nums[mid] Hence, mid is the smallest. 

class Solution:
    # O(logn) approach
    def findMin(self, nums: List[int]) -> int:
       # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
                
                       