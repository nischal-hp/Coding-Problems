# Same as Two Sum problem. But here the array is sorted in non-decreasing (increasing) order.
# Also the array is 1-indexed, meaning the index starts from 1, and not 0.
# The returned indices must be in increasing order as well. Same number cannot be used twice.

class Solution:
    def twoSumII(self,nums,target):
        seen={}
        for i,value in enumerate(nums):
            remaining = target-value
            if remaining in seen:
                return[seen[remaining]+1,i+1] # Add +1 to the return value, since it is 1-indexed.
                #  Also since we want output in increasing order, make sure to have seen value first and current index later on. 
            else:
                seen[value]=i


# Another Approach - Two Pointer Approach (Since the array is sorted)
# We see the following approach in a lot of problems. What you want to do is to have two pointer (if it was 3sum, 
# you'd need three pointers). One pointer move from left and one from right. 
# Let's say you numbers = [1,3,6,9] and your target = 10. Now, left points to 1 at first, and right points to 9. 
# There are three possibilities. If you sum numbers that left and right are pointing at, you get temp_sum (line #1). 
# If temp_sum is your target, you'r done! You're return it (line #9). If it's more than your target, it means that right is 
# pointing to a very large value (line #5) and you need to bring it a little bit to the left to a smaller (r maybe equal) 
# value (line #6) by adding one to the index . If the temp_sum is less than target (line #7), 
# then you need to move your left to a little bit larger value by adding one to the index (line #9). 
# This way, you try to narrow down the range in which you're looking at and will eventually find a couple of number 
# that sum to target, then, you'll return this in line #9. 
# In this problem, since it says there is only one solution, nothing extra is necessary. 
# However, when a problem asks to return all combinations that sum to target, you can't simply return the first instace and you need to collect all the possibilities and return the list altogether (you'll see something like this in the next example).

# Time Complexity is still O(n), but space complexity is O(1), as we are not using any extra variables.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            left=0
            right=len(numbers)-1
            while left<right:  # Important to check this so that there is no cross over of left and right indices
                temp_sum=numbers[left]+numbers[right] # left, right are indices. So to access the actual value used numbers[left] here
                if temp_sum>target:
                    right-=1
                elif temp_sum<target:
                    left+=1
                else:
                    return[left+1,right+1]

