# Easy Problem : Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Ex 1 :
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Ex 2 : 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Solution 1 : It follows a similar approach to Same Tree Problem. If we were to employ brute force solution, we go on iterating
# the root Tree and if the value matches with the subRoot Tree, we then check the value of the left and right subnodes and iteratively continue the process.
# Time : O(m*n), where m,n - number of nodes in each tree.

# Edge Cases to consider :
# 1) If subRoot is None, then we have to return True irrespective of whether root is None or not.
# Because a null tree is a subtree of any tree
# 2) If root is None and If subRoot is not None, then have to return False; since subRoot cannot exist is root.

# A helper function is needed to check if the two subtrees are same. This helper function is same as solving SameTree leetcode problem.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:    # Edge Case 1
            return True
        if not root:       # Edge Case 2
            return False
        if self.isSameTree(root,subRoot):  # If both trees are same, return True
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) # If both trees are not same, check with the left/right subtree of root
        
    def isSameTree(self,s,t):   # Helper Function same as SameTree leetcode problem
        if not s and not t:     # If both are Null, means both are same trees. Hence return True.
            return True
        if s and t and s.val==t.val:   # If both nodes exist and values are same. Recursively go to left and right subtrees
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)
        return False       # If above 2 conditions dont match, return False

# Solution 2 : Linear approach O(m+n)
# We make a recursive traverse_tree function that will return a string representation of a tree, and then we just need to convert both trees to strings and check if tree t is substring of tree s
# This is bacisally converting tree into a string and then checking if one exists within the other or not.

# IMP : # is to be added before the value, in order to differentiate the case where values can be 2 and 12. Here if we run if 2 is in 12, it will return True, which is wrong.
# However by adding #, #2 is not in #12, so we can overcome this issue intelligently.

# Time : O(m) and O(n) for traversing the trees. Python's substring search (e.g. if substring in string) runs in O(n) time on average, with O(n*m) being the worst case, with n being the longer string and m the shorter string.
# So the average case is O(m+n+n), which is linear.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        string_s = self.traverse_tree(root)   # Convert two trees into a string representation
        string_t = self.traverse_tree(subRoot)
        if string_t in string_s:    # Check if substring is present within string or not
            return True
        return False
    
    
    def traverse_tree(self, s):
        if s:     # If node exists, build a string representation like below
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"  # IMP step: To add a # before the value
        return None    # If node does not exist, return None
        
        