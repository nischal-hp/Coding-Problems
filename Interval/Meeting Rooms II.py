# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# (0,8),(8,10) is not conflict at 8

# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
# Example2

# Input: intervals = [(2,7)]
# Output: 1
# Explanation: 
# Only need one meeting room

# Solution 1 : O(nlogn) time. O(n) space
# We cant just implement the foll. soln based on Meeting Rooms 1 problem :
# def meeting_rooms(intervals):
#     rooms = 1
#     intervals.sort()
#     for i in range(1,len(intervals)):
#         if intervals[i][0] <= intervals[i-1][1]:
#             rooms+=1
#     return rooms

# This is because, the no of meetings at any given point of time, also depends on the end time of the prev meetings.
# Hence, we store 2 arrays in sorted order, of start time and end time.
# We use 2 variables, and check the min of the first element of start n end time. 
# If start time array has min value, then we increment the count of rooms by 1.
# If end time array has min value, then we decrement the count of rooms by 1. 
# If there is a tie, that is value in start time array== value in end time array, then we first have to travel through end time array, then go to start time array.
# At the end, result is the max of count whenever that occured.

def meeting_rooms(intervals):
    start = []
    end = []
    for s,e in intervals:
        start.append(s)
        end.append(e)
    start.sort()
    end.sort()
    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res

print(meeting_rooms([(0,30),(5,10),(15,20)]))
print(meeting_rooms([(5,8),(9,15)]))