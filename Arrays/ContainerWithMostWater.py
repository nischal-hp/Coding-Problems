# (11. Medium) You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Ex 1 :
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# Solution 1: O(n^2) time
# Iterate through each element, and check the maxArea with every other element coming after it.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n^2) soln
        maxArea=0
        for i in range(len(height)):
            for j in range(i,len(height)):                  
                maxArea = max(maxArea,min((j-i)*height[j],(j-i)*height[i]))
        return maxArea

# Soln 2 : O(n) time. 2-pointer approach
# Since we want to maximize area, we start off with the largest width possible. Hence left pointer at starting value, and right pointer at ending value.
# Next, we shift the pointer based on whichever is the lowest value, so as to maximize the area.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) soln
        maxArea=0
        l=0
        r=len(height)-1
        while l<r:                
                maxArea = max(maxArea,min((r-l)*height[l],(r-l)*height[r]))
                if height[l]<height[r]:
                    l+=1
                else:
                    r-=1
        return maxArea
        