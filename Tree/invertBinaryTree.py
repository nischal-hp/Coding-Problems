# Given the root of a binary tree, invert the tree, and return its root.

# Ex 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Ex 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Ex 3:
# Input: root = []
# Output: []

# Solution 1 : Recursive 
# If we observe the problem, at each stage we swap the left and right subtrees.
# We go on doing it, until we reach the end of the tree.
# THis can be easily implemented using recursive approach.

class Solution:
    def invertTree(self,root):
        if not root:          # Base case : When root is None
            return None 
        root.left,root.right = root.right,root.left  # Swap the 2 subtrees
        self.invertTree(root.left)   # Recursively call the function on left and right subtrees
        self.invertTree(root.right)
        return root     # Finally return the root

# Solution 2 : Iterative. DFS approach using stack

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])   # IMP : Make sure to append in reverse order
        return root

# Solution 3 : Iterative. BFS approach using queue
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root