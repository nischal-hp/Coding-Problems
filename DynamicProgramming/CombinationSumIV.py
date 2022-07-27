# (377. Medium) Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

# Solution 1 : DP. O(n) space, O(n*m) time. where n-target, m-nums array length
# If we write the recursion tree for this problem. Ex : nums[1,2,3], target = 4
# Starting from 0, we can explore all the 3 paths and then observe the sum.
# Stop going down a certain path, if we encounter a value = target, or if its more than target.
# We don't need to repeat the process for 2 and 3 again. Coz, from 1, we would have explored 1,2,3 paths.
# 1+1=2, 1+2=3 are already covered.
# Thus we can use memoization to make use of the previously stored values.
# Coverting this tree into a dp problem. If we take bottom up-approach, we start from 0 and go all the way to target.
# dp[0] =0, since number of combinations to make 0 is 0.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ## RC ## 
        ## APPROACH : DP ##
        # 1. Base case : Number of combinations to make 0 is 0.
        # 2. consider nums= {1,2,3}
        # 3. target = 1, combinations = {1}
        # 4. target = 2, combinations = {1,1}, {2}
        # 5. target = 3, combinations = {1,1,1} , {1,2}, {2,1}, {3}
        # 6. If number is in the list, you can directly count it as one combination
        # 7. else include all the combinations of target - nums[i]
        
		## TIME COMPLEXITY : O(N*M) ##
		## SPACE COMPLEXITY : O(N) ##

        dp = [0] * (target+1) 
        for i in range(1, target+1):            # offset from 1 to skip base case (first element)
            for n in nums:
                if( n == i):                    # If number is in the list, you can directly count it as one combination
                        dp[i] += 1
                if n < i:                       
                        dp[i] += dp[i-n]        # include all the combinations of target i-n.
        return dp[-1]