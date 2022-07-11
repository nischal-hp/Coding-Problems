# (435. Medium) Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
# Constraints:
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4

# Solution 1 : Brute Force. 2^n time
# Iterate through the array, and then decide whether we want to keep the current array element or not.
# At each point we can make 2 decisions - either to keep it or not. This makes it 2^n

# Solution 2 : O(nlogn) time. Sort
# 1. Sort the array. Then we have to keep track of prev end elem using a variable
# 2. There is no overlap if the end value of current element is >= end value of prev elem.
# In this case, update the end value variable to be the end value of the curr elem.
# 3. If there is overlap, then increment the result counter.
# IMP : We want to remove the one which has larger end value. Since it can cause further overlappings down the road.
# Hence, while updating the end value variable in this case, take the minimum of the curr end value or the prev end value variable. Since, the max one would be deleted and we dont need it.

class Solution:
    # O(nlogn) solution
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res =0
        intervals.sort()
        prevEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if prevEnd<=intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                res+=1
                prevEnd = min(prevEnd,intervals[i][1])
        return res

# Solution 3 : Same as above, but sort by end time.
# If we think more clearly, the first solution can be improved slightly (save a line of code) by sorting the intervals with end time. Why? Becuase the greedy nature remains true even if we the remaining array is not sorted by start time. Meanwhile, if we sort them by end time and if overlap occurs, the interval that comes later must be the one to remove as it has larger end time. 
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans