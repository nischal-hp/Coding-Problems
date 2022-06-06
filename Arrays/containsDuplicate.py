# Array Problem

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Solution 1) Using set: 
# Use a set data structure in Python to remove the duplicates. Then just compared the length of the original array with 
# length of set
# Time Complexity - O(n). Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_array=set(nums)
        if len(new_array)!=len(nums):
            return True
        else:
            return False


# Solution 2) Sorting the array:
# Sort the array. Iterate through it, and check if two values one after the other are same or not.
# Time Complexity - O(nlogn). Space - O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                contains = True
        return contains

# Solution 3) Using Counter:
# Counter is a subclass of dict designed for counting hashable objects in Python. It’s a dictionary that stores the objects as keys and the frequencies of those objects as values. 
# In this approach, we utilize Counter to count the frequencies of each integer for us. For example, if the input array is [1, 2, 3, 4, 4, 5], using Counter on that input array will give us the following dictionary: Counter({4: 2, 1: 1, 2: 1, 3: 1, 5: 1}). Utilizing this function, we will loop through the freq dictionary to see if any values (frequencies) are greater than 1, which means there exists an integer in the given array that is duplicated.

def containsDuplicate(self, nums: List[int]) -> bool:
    freq = Counter(nums)
    for num, freq in freq.items():
        if freq > 1:
            return True
    return False

# Solution 4) Using Hashmap:
# In this approach, we essentially mimick what the Counter function does in the previous approach. We first initialize a hashmap, to which we loop through the given array and plot the frequencies of each integer by incrementing the values in the hashmap. 
# Then, we try to look for a frequency that is greater than 1 and return the result accordingly.

def containsDuplicate(self, nums: List[int]) -> bool:
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
    for num, freq in counter.items():
        if freq > 1:
            return True
    return False
