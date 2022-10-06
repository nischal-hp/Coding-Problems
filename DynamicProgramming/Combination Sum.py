# (39. Medium) Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 
# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 500

# Solution : Using Decision Tree. Ex : candidates = [2,3,5], target = 7
# Suppose we build a decision tree, and at each step, we can consider all the numbers in candidates list.
# We stop going down a path, if we go above target. If the combination == target, we append it to the result array.
# The problem with this is, there might result in a duplicate combination. Ex: [2,2,3] and [2,3,2] both will be appended to the result.

# Solution : 2^(n) time and space, where n is length of candidates. DFS with backtracking
# To overcome above problem, we build the decision tree differently.
# We start with an empty array. At each step, we make 2 decisions: To include an element; and to not include that element, but consider the rest of the array.
# Hence time complexity becomes 2^n.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return 
            for i in range(index, len(candidates)):  # Since we are starting from index, we are including the current element as well; thus allowing for repetition
                dfs(target-candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return res
        