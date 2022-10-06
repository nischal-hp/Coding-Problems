# (124. Hard) A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Ex 1 : Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Ex 2 : Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000

# Solution using DFS : O(n) time, O(h) - space. h-height of tree. for balanced tre, h is log(n)
# We have to recursively find the max path sum possible from each node.
# While calculating the result, we can include the root, left and right subtree values.
# But if we are to return the value to its parent node. THen we can only pick one path. Thus will have to pick the max btw left and right subtree.
# This is coz, once we go along left subtree, we can't return back to root and go along right subtree; as each node can only be traversed once.

# Refer the Binary Tree Max Path Sum.JPG File : 
# The value marked in blue next to a node, is the max path possible from that node, which is used to compute result.
# However while returning the value from node 3 to 1, we can only consider either left or right subtree value, not both.
# Hence have to pick the max btw 4 and 5; add that to 3, and then return it.

# Both 4 and 5 could be negative as well. In that case, to handle negative cases, we first take the max btw 0 and the value of the node.
# Thus when 0 is added to root value, no changes happen.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # Update the max variables, to handle the case with -ve values.
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Compute the result without including the split
            res[0] = max(res[0], leftMax + root.val + rightMax)
            
            # Return value has to be including the split. So will have to choose max btw left and right tree
            return root.val + max(leftMax,rightMax)
        
        dfs(root)
        return res[0]
        