# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Ex 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Ex 2:
# Input: root = [1]
# Output: [[1]]

# Ex 3:
# Input: root = []
# Output: []

# Solution : The approach is very similar to the maxDepthBinaryTree problem. We need to do level order traversal using BFS.
# Need to hold a temp variable which creates a list of values for each level, which then has to be appended to the main list.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level= [root] if root else []  # Array holding the elements in each level
        stack=[[root.val]] if root else []
        while level:
            queue=[]     # Refresh queue variable after each level
            temp=[]      # Refresh temp variable after each level
            for el in level:
                if el.left:
                    queue.append(el.left)   # Pop elements into queue if they exist
                    temp.append(el.left.val)   # Append the values to the temp variable created
                if el.right:
                    queue.append(el.right)
                    temp.append(el.right.val)
            if temp!=[]:
                stack.append(temp)       # Make sure to check the case where array can be empty too
            level=queue     # Go to the next level
        return stack 

# Same Solution. Using Queue : 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, ans = deque([root] if root else []), []
        while len(queue):
            qlen, row = len(queue), []      # When we come back to this point, we would have visited all the nodes in a level
            for _ in range(qlen):
                curr = queue.popleft()
                row.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(row)
        return ans
            