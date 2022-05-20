# Array
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such 
# that nums[i] == nums[j] and abs(i - j) <= k. 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Solution 1) Using Dictionary : 
 #This algorithm works by creating a dictionary for all the numbers in nums
# In this dictionary, the number is the key and the number's index is the value
# The algorithm loops through all the elements, and for each element, it checks if the
# Element is already in the dictionary. If it is, then it checks if the index of this
# duplicate number is within the range of k. If thats true, it returns true. if not,
# it updates the last seen index of the number or creates a new key for the number.

# Time Complexity: O(n). Space/Memory complexity is O(the number of distinct numbers) because the dictionary
# will only hold distinct elements in there. Many people would just simplify this to O(n) because the worst case is that each element is distinct, but this is the specificmemory complexity.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct_nums = {}
        for i, num in enumerate(nums):
            if num in distinct_nums:
                if abs(distinct_nums[num] - i) <= k:
                    return True
            distinct_nums[num] = i # create/update index of num

# Solution 2) Sliding Window Solution with set  
# Sliding window with 'fixed' set length of k (because of index difference of k)

# O(N) Time Complexity
# O(1) Memory using fixed set length vs O(N) memory with solutions using dictionary

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        for i in range(len(nums)):
            if len(numSet) > k:                   #if length of Set goes beyond abs(i - j) <= k
                numSet.remove(nums[i-(k+1)])        #remove first value of Set (no longer in conditions to compare with current iteration)
            if nums[i] in numSet:                 #if current iteration in Set (set was just assured to be in bounds of condition abs(i - j) <= k)
                return True                         #return True if in Set
            numSet.add(nums[i])                   #if not, add current iteration to Set
        return False                      #if not found return False