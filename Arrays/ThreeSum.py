# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Naive Soln is O(n3). Have 3 diff loops running through the array. We check the sum a every stage, and it to the result

#Here, instead of looping (line #1) to len(nums) -1, we loop to len(nums) -2 since we're looking for three numbers. Since we're returning values, sort would be a good idea. Otherwise, if the nums is not sorted, you cannot reducing right pointer or increasing left pointer easily, makes sense?

#So, first you sort the array and define res = [] to collect your outputs. In line #2, we check wether two consecutive elements are equal or not because if they are, we don't want them (solutions need to be unique) and will skip to the next set of numbers. Also, there is an additional constrain in this line that i > 0. This is added to take care of cases like nums = [1,1,1] and target = 3. If we didn't have i > 0, then we'd skip the only correct solution and would return [] as our answer which is wrong (correct answer is [[1,1,1]].

#We define two additional pointers this time, left = i + 1 and right = len(nums) - 1. For example, if nums = [-2,-1,0,1,2], all the points in the case of i=1 are looking at: i at -1, left at 0 and right at 2. We then check temp variable similar to the previous example. There is only one change with respect to the previous example here between lines #5 and #10. If we have the temp = target, we obviously add this set to the res in line #5, right? However, we're not done yet. For a fixed i, we still need to check and see whether there are other combinations by just changing left and right pointers. That's what we are doing in lines #6, 7, 8. If we still have the condition of left < right and nums[left] and the number to the right of it are not the same, we move left one index to right (line #6). Similarly, if nums[right] and the value to left of it is not the same, we move right one index to left. This way for a fixed i, we get rid of repeative cases. For example, if nums = [-3, 1,1, 3,5] and target = 3, one we get the first [-3,1,5], left = 1, but, nums[2] is also 1 which we don't want the left variable to look at it simply because it'd again return [-3,1,5], right? So, we move left one index. Finally, if the repeating elements don't exists, lines #6 to #8 won't get activated. In this case we still need to move forward by adding 1 to left and extracting 1 from right (lines #9, 10).

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums) -2): #1  
            if i > 0 and nums[i] == nums[i-1]: #2   # To check for the repeating value.
                continue
            left = i + 1 #3
            right = len(nums) - 1 #4
            
            while left < right:  
                temp = nums[i] + nums[left] + nums[right]
                                    
                if temp > 0:
                    right -= 1
                    
                elif temp < 0:
                    left += 1
                
                else:
                    res.append([nums[i], nums[left], nums[right]]) #5
                    while left < right and nums[left] == nums[left + 1]: #6 # Look for repititive numbers and change pointer values
                        left += 1
                    while left < right and nums[right] == nums[right-1]:#7
                        right -= 1    #8
                
                    right -= 1 #9 #Once we have found the right result, we can change the pointer values of both left and right.
                    # That is skip the current characters since they are already in the result array
                    left += 1 #10


#Another way to solve this problem is to change it into a two sum problem. Instead of finding a+b+c = 0, you can find a+b = -c where we want to find two numbers a and b that are equal to -c, right? This is similar to the first problem. Remember if you wanted to use the exact same as the first code, it'd return indices and not numbers. Also, we need to re-arrage this problem in a way that we have nums and target.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            output_2sum = self.twoSum(nums[i+1:], -nums[i])
            if output_2sum ==[]:
                continue
            else:
                for idx in output_2sum:
                    instance = idx+[nums[i]]
                    res.append(instance)
        
        output = []
        for idx in res:
            if idx not in output:    # To remove the repeating elements from the result
                output.append(idx)
                
        
        return output
    
    
    def twoSum(self, nums, target):
        seen = {}
        res = []
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
           
            if remaining in seen: #3
                res.append([value, remaining])  #4
            else:
                seen[value] = i  #5
            
        return res            # Return back all possible combinations of sum