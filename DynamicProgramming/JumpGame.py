# (55. Medium) You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

# Solution 1 : Brute Force using Cache O(n^2)
# If we draw a decision tree. For Ex: [2,3,1,1,4].
# Starting at index 0, we can take a jump of either 1 or 2. Next from index 1, we can take a jump of 1,2 or 3.
# If we are able to reach the end, we can store the dp value as True. Else it becomes False.
# We can use cache to make sure, that we dont re-calculate already calculated values.
# We finally have to check if dp[0]==True or not.

# Solution 2 : Greedy : O(n) time
# Instead of starting from first, we can start from the goal which is the end, and work our way backwards.
# We iterate the array in reverse order, and at each index, we check if the value at index+ index >= goal.
# If so that means we can reach our goal, now we can update our goal to be equal to index value.
# Finally, if our goal becomes 0, that means we have found a path.

class Solution:
    # O(n) time, Greedy Solution
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        return True if goal==0 else False
                    
        