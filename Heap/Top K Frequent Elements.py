# (347. Medium) Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 
# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Solution 1 : O(n) time and space. Without using heap. Using an array, whose index specifies the count of an integer in nums.
# First we build a dictionary which has the count of each integer in nums.
# Next we build an array, where each index represents the count; and each value is an array.
# The array size is equal to the size of nums+1 (len(nums)+1), this is because if size of nums== 2, then if same integer is contained, the max count is 2.
# Iterate through dictionary, and append proper values to the array.
# Next iterate through the array in reverse order, and append it to the result array.
# WHen len of result array==k, we have to stop

class Solution:
    # O(n) time, O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
# Solution 2 : Using heap O(nlogk) time, O(n) space
# Build a frequency dictionary (freq is positive)
# Build a heap
# Make sure heap conatins k items at maximum by popping out the items with least frequency as you push to heap
# The time complexity of adding an element in a heap is O(log(k)) and we do it N times that means O(Nlog(k)) time complexity for this step.
# Heap now contains k items (the desired output basically)
# Pop and append to the output list - O(klog(k))
# return list

# Heap (h) grows like this, for the example : nums = [1,1,1,2,2,3] and k = 2 :
# []
# [(3, 1)]
# [(2, 2), (3, 1)]

class Solution:
    # O(nlogk) time, O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
                    return [nums[0]]

        # freq dict
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # insert k items into heap O(nlog(k))
        h = []
        from heapq import heappush, heappop
        for key in d: # O(N)
            print(h)
            heappush(h, (d[key], key)) # freq, item - O(log(k)) # IMP : h here stands for heap
            if len(h) > k:
                heappop(h)

        res = []
        while h: # O(k)
            frq, item = heappop(h) # O(logk)
            res.append(item)
        return res