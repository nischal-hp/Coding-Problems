# (128. Medium) Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# Solution 1 : Brute Force. O(n^3) time, O(1) space
# Because a sequence could start at any number in nums, we can exhaust the entire search space by building as long a sequence as possible from every number.
# The brute force algorithm does not do anything clever - it just considers each number in nums, attempting to count as high as possible from that number using only numbers in nums. After it counts too high (i.e. currentNum refers to a number that nums does not contain), it records the length of the sequence if it is larger than the current best. The algorithm is necessarily optimal because it explores every possibility

# Time : O(n^3), The outer loop runs exactly O(n) times, and because number increments by 1 during each iteration of the while loop, it runs in O(n) time. Then, on each iteration of the while loop, an O(n) lookup in the array is performed. Therefore, this brute force algorithm is really three nested O(n) loops, which compound multiplicatively to a cubic runtime.
# Space : O(1)

class Solution:
    # Brute Force
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for number in nums:
            cur_longest = 1
            number+=1
            while number in nums:
                cur_longest+=1
                number+=1
            longest = max(longest,cur_longest)
        return longest

# Solution 2 : Using Sorting. O(nlogn) time, O(1) space
# Sort the array, and then find the longest possible subsequence in the sorted array

class Solution:
    # Using Sorting
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        cur_streak = 1
        if not nums:  # If the list is empty
            return 0
        nums = sorted(nums)
        i=1
        while i<len(nums) and len(nums)>1:
            if nums[i] != nums[i-1]:  # IMP : To account for the case of [1,2,0,1]. We only need to account for increasing elements
                if nums[i]==nums[i-1]+1:
                    cur_streak+=1
                else:
                    cur_streak=1
                longest = max(longest,cur_streak)
            i+=1
            
        return longest

# Solution 3 : O(n) Time, O(n) Space
# The intuition is that, we have to find the start of the seq. If there is no element equal to current element's value-1, then it means its the start of the seq.
# To perform O(1) lookup on the array, we can store the array on the set. 
# Once we have the start of sequence, we check if a number equal to current element's value+1 exists or not, and then continue this to find the length of longest seq.

class Solution:
    # Using Hash Set. O(n) Time and Space
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 1
        if not nums:
            return 0
        for number in nums:
            if number-1 not in numSet:
                number+=1
                cur_streak = 1
                while number in numSet:
                    cur_streak+=1
                    number+=1
                longest=max(longest,cur_streak)
        return longest