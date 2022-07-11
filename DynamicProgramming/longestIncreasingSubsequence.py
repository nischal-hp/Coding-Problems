# (300. Medium) Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 
# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# Solution 1 : Brute Force, DFS : O(2^n) time, O(n) space - TLE - A bit difficult to understand
# At every index, we have a choice to make, We can either include the element in the LIS(longest increasing subsequence) or not.
# Using this we can find all the different possible combination of subsequences and then find the max out of it.
# This will be O(2^n) time. Since we can make 2 different choice at each index.

def lengthOfLIS(self, nums) -> int:
	def max_lis(idx, cur_max):
		if idx == len(nums):  # Base Case, when we have exceeded the length of nums
			return 0
		if nums[idx] > cur_max:
			return max(1 + max_lis(idx + 1, nums[idx]), max_lis(idx + 1, cur_max))
		return max_lis(idx + 1, cur_max)
	return max_lis(0, float('-inf'))

# Solution 2 : Recursion with memoization (DP): time O(n^2) space O(n^2) - TLE - A bit difficult to understand
from collections import defaultdict
def lengthOfLIS(self, nums) -> int:
	cache = defaultdict(dict) # 2D cache of prev_max_idx & cur_idx
	nums.append(float('-inf'))
	def max_lis(idx, prev_max_idx):
		if idx == len(nums) - 1:  # Since last element is float('-inf')
			return 0
		if prev_max_idx not in cache or idx not in cache[prev_max_idx]:
			if nums[idx] > nums[prev_max_idx]:
				cache[prev_max_idx][idx] = max(1 + max_lis(idx + 1, idx), max_lis(idx + 1, prev_max_idx))
			else:
				cache[prev_max_idx][idx] = max_lis(idx + 1, prev_max_idx)
		return cache[prev_max_idx][idx]
	return max_lis(0, -1)

# Solution 3 : DP with Top Down Approach. O(n^2). Space : O(n)
# Consider ex : nums=[1,2,4,3]. We can start from the last element, which will be the base case. LIS[3]=1, since only one possible
# element is present and there is no element after that in the array.
# Coming to LIS[2]. We now have to iterate through the rest of the array starting from index 2.
# if nums[3]>nums[2]: LIS[2]=max(1,1+LIS[3])=1, since nums[3]<nums[2]
# Repeating it for index 1, LIS[1]=max(1,1+LIS[2],1+LIS[3])=max(1,2,2)=2
# Repeating it for index 0, LIS[0] = max(1,1+LIS[1],1+LIS[2],1+LIS[3]) = max(1,3,2,2)= 3
# Finally will have to return the max element in the list LIS[], which is 3

class Solution:
    # DFS with Top Down. Time: O(n^2), Space : O(n)
    def lengthOfLIS(self, nums) -> int:
        LIS=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)

# Solution 4 : Same as above, but with Bottom Up- approach
def lengthOfLIS(self, nums) -> int:
	if not nums:
		return 0
	dp = [1] * len(nums)
	max_len = 1
	for i in range(1, len(nums)):
		for j in range(0, i):
			if nums[j] < nums[i]:
				dp[i] = max(dp[i], dp[j] + 1)
		max_len = max(max_len, dp[i])
	return max_len

# Solution 5 : Above approach can be further optimized.
# Bottom Up + Binary Search. time O(nlogn) space O(n)
# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

# len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
# len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
# len = 3   :      [4, 5, 6]            => tails[2] = 6
# We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

# Each time we only do one of the two:

# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
# Doing so will maintain the tails invariant. The the final answer is just the size.


    # DP+Binary Search. Time: O(nlogn), Space : O(n)
def lengthOfLISbinary(nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

lengthOfLISbinary([1,2,4,3])
