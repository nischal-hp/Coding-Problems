# (56. Medium) Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4

# Solution 1 : O(nlogn) time, O(n) space
# We first have to sort the intervals array based on the start value, since it is not guaranteed to be in ascending order 
# Start from second element onwards. Check if its less than or equal to prev elements last value.
# If so, update the merged interval, and continue with the process.
# If there is no merge to be done, append directly to result array.

class Solution:
    # Time : O(nlogn), space : O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        result=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = result[-1][1]
            if start<=lastEnd:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start,end])
        return result

# Solution 2 : O(nlogn) time, O(1) space
# Same as before. But modify the input array directly, instead of using another result array

class Solution:
    # Time : O(nlogn), space : O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda item: item[0])

        i = 0
        # no neeed to check the last array
        while (i + 1) < len(intervals):

            curr_a = intervals[i]
            next_a = intervals[i+1]

            # check for overlap
            if curr_a[1] >= next_a[0]:

                # merge
                # we use max coz of such a case: [[1,4],[2,3]]
                # make the last element of the first array be the furthest(largest value)
                intervals[i][1] = max(curr_a[1], next_a[1])

                # delete the second array
                intervals.pop(i+1)

            else:
                i += 1

        return intervals
                
        
        