# (57. Medium) You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starting point in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5


# Solution : O(n) time. O(n) space if we include the result set
# We go traversing through the intervals list. There are 3 possibilities which exists:
# 1) There is overlap between the current interval and the newInterval. In that case, we have to calculate the newInterval, and then go on with the process. We can't append it to the res yet.
# 2) There is no overlap. But the ending of newInterval is less than starting of current interval. This means that newInterval and all the other intervals which comes after the current interval can be directly appended to the result and returned.
# 3) There is no overlap. But the ending of current interval is less than starting of newInterval. This means we can append the current interval, but have to continue with the process.
# Finally, append the newInterval, as the loop can exit out, without appending the newInterval, if its the last interval which overlaps, that is, Case 1 happens at the last iteration.


class Solution:
    # O(n) solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if intervals[i][0]<=newInterval[0]<=intervals[i][1] or intervals[i][0]<=newInterval[1]<=intervals[i][1]:  # Case 1
                newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
            elif newInterval[1]<intervals[i][0]: # Case 2
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]: # Case 3
                res.append(intervals[i])
        # Finally append the newInterval to the res and return it
        res.append(newInterval)
        return res
                

class Solution:
    # O(n) solution - A more cleaner solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]: # If there is no overlap, but starting point of current interval is more than ending point of newInterval
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]: # If there is no overlap, but starting point of newInterval is more than ending point of current interval
                res.append(intervals[i])
            else: # If there is an overlap, then find the newInterval
                newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
        # Finally append the newInterval to the res and return it
        res.append(newInterval)
        return res

# Solution 2 : O(1) space using Binary Search, if we dont count the O(n) with list slicing. 
# But if we count that as well, true O(n) space soln might not exist.
# Binary Search : find the intervals new_interval overlap with : insert_start=i, insert_end=j 
# Update new_interval  and return [0 : i[ + new_interval + ]j : n] 

def __init__(self):
	self._start, self._end = 0, 1 # interval start and end indexes

def _binary_search(self, intervals: List[List[int]], val, l=0, r=None):
	if r is None:
		r = len(intervals) - 1
	
	while l <= r:
		mid = (l + r) // 2
		if intervals[mid][self._start] <= val <= intervals[mid][self._end]:
			return mid
            
		elif val > intervals[mid][self._end]:
			l = mid + 1
                
		else:
			r = mid - 1
        
	return l

# Solution 1:
def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:

	intervals_count = len(intervals)
	
	# 1. Search the interval where new_interval.start fits in: O(logn) time
	val = new_interval[self._start]
	insert_start = self._binary_search(intervals, val)
	if insert_start < intervals_count and intervals[insert_start][self._start] <= val <= intervals[insert_start][self._end]:
		new_interval[self._start] = intervals[insert_start][self._start]
		new_interval[self._end] = max(intervals[insert_start][self._end], new_interval[self._end])        
	
	# 2. Search the interval where new_interval.end fits in: O(logn) time
	val = new_interval[self._end]
	insert_end = self._binary_search(intervals, val, insert_start)
	if insert_end < intervals_count and intervals[insert_end][self._start] <= val:
		new_interval[self._end] = max(intervals[insert_end][self._end], new_interval[self._end])
		insert_end += 1
	
	# 3. Replace overlapping intervals with new_interval: O(n) time and O(1) space
	intervals[insert_start:insert_end] = [new_interval]
	
	return intervals
                
        
        