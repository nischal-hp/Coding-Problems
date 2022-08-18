# (268. Easy) Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

# Constraints:

# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# Solution 1 : O(n) time, O(1) space - using sum property
# We can use the gaussian formula to find the sum of n numbers in a series starting from 0 : (n*(n+1))//2
# Then find the actual sum of the series and subtract the 2, to get the missing number

class Solution:
    # O(n) time, O(1) space - using sum property
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n*(n+1))//2 - sum(nums)

# Solution 2 : Using XOR operator. O(n) time, O(1) space
# Intution:
# XOR is a bitwise operation.
# The output is true when two values are not the same (exclusive) E.g 1^0 = 1 , 1^1 =0 , 2^0 = 2 , 2^2 = 0.
# Value that is XOR with itself is 0

# XOR operations are commutative :
# 1^1^2 == (1^1)^2 == (2^1)^1 == 2
# Order does not mater when you use XOR, if there are two instances of the same number, the XOR operations cancel each other out to get 0

# We are essentially doing XOR of the complete sequence (which is nothing but index+1) with the result variable. Then we XOR result with each number from the numList .
# Same values from complete sequence and numList cancel each other and the missing number manifests iteself.

class Solution:
    # O(n) time, O(1) space - using xor property
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for index,value in enumerate(nums):
            result ^= index+1
            result ^= value
        return result