# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Note :
# (0,8),(8,10) is not conflict at 8

# Example :
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation: 
# (0,30), (5,10) and (0,30),(15,20) will conflict
# Example2

# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation: 
# Two times will not conflict 

# Solution 1 : O(nlogn) time
# Sort the array based on start time, if its not already sorted.
# Check at each instance, whether the new start time is greater than prev end time.

def can_attend_meetings(intervals):
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0] <= intervals[i-1][1]:
            return False
    return True


print(can_attend_meetings([(0,30),(5,10),(15,20)]))
print(can_attend_meetings([(5,8),(9,15)]))