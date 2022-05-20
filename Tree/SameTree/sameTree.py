# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Ex 1 :
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Ex 2 :
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Solution 1: Recursion
# Check if both nodes are None, return True. If one of the nodes in None, return False.
#  If values are not equal, return False.
# Call recursive function on both left and right subtree using and function

# Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.

# Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


# Solution 2 : Iterative : 
# Start from the root and then at each iteration pop the current node out of the deque. Then do the same checks as in the approach 1 :
# and if checks are OK, push the child nodes.

# Time and Space complexity are same as before.

from collections import deque
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:   # Check Done so that we don't append when it is None                            
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True
