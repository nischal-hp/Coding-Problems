# (207. Medium) There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# Solution : Using DFS 
# Firstly we can maintain a map which maps the course to its prereq's.
# Next we can call DFS for each of the courses. This is because, it can be an unconnected graph. Hence, need to check for all the nodes.
# For each course, find its prereq, then iteratively call DFS on it, until it is empty list, which is the base case.
# Also maintain a set which contains the nodes in the current path of DFS.
# If we encounter a node which is already in the set, it means there is a cycle in the graph, and courses cant be completed, so can return False.
# Otherwise keep repeating for all the courseNumbers.

class Solution:
    # DFS solution
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)} # Map each course to prereq list
        for course,pre in prerequisites:
            preMap[course].append(pre)
        
        visitedSet = set() # All courses along the current DFS path
        def dfs(crs):
            if crs in visitedSet:  # Base Case 1
                return False
            if preMap[crs]==[]:  # Base Case 2
                return True
            visitedSet.add(crs)   # Add it to the set
            for pre in preMap[crs]:
                if not dfs(pre): return False  # Call dfs recursively on each of the prereq
            visitedSet.remove(crs)  # Finally remove it from the set
            preMap[crs]=[]       # Since we know this course can be completed, we can set its value to [] to simplify the process and make it faster
            return True
        for crs in range(numCourses):  # Has to be called on every course, as it can be an unconnected graph
            if not dfs(crs): return False
        return True
    
        
        