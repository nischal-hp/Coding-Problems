# (98. Medium) Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Ex 1 :
# Input: root = [2,1,3]
# Output: true

# Ex 2 :
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:

# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

# Solution 1 : A wrong solution O(n)
# We cant just check if the current node's left value is less than current val, and right val is greater then current val.
# We also have to make sure, that the entire right subtree has values greater than root node.
# Below is the wrong solution, which will break in few cases
class Solution:
    # O(n) solution
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.left.val>=root.val:
            return False
        if root.right and root.right.val<=root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

# Solution 2 : Brute Force O(n^2)
# Starting at every node, check if all the values to the left of it, is less than it; and all the values to right of it is greater than it.
# Since, we have to repeat this at every node. Time complexity becomes O(n^2)

# Solution 3 : DFS O(n)
# Modifying solution 1, we need to have 2 variables - one to keep track of minVal, and other to keep track of maxVal.
# Initially start out with minVal = float('-inf') and maxVal = float('inf')
# While iterating left subtree, we need to update the maxVal to be the current node's value.
# While iterating right subtree, we need to update the minVal to be the current node's value.
# This will help eliminate the edge case, which caused solution 1 to be wrong.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) solution
    def isValidBST(self, root: Optional[TreeNode], minVal= float('-inf'), maxVal=float('inf')) -> bool:
        if not root:
            return True
        if not (minVal<root.val and root.val<maxVal):   # Check for the breaking case and return False there
            return False
        return self.isValidBST(root.left,minVal,root.val) and self.isValidBST(root.right,root.val,maxVal)

# Solution 4 : Not efficient. Using in-order traversal method. O(nlogn) time and O(n) space
# As inorder traversal of a bst is always sorted we check this first and return True and False based on that.
# For this 68/80 testcases passed. Testcases like [2,2,2] failed.

# So, We check if all elements are unique or not using hashmap/dictionary and return True/False based on these 2 points.


class Solution:
    # O(nlogn) time and O(n) space
    def isValidBST(self, root: Optional[TreeNode], minVal= float('-inf'), maxVal=float('inf')) -> bool:
        # Inorder Traversal method : O(nlogn) time and O(n) space
        ans = []
        def intraversal(self,root):
            if root is None:
                return 
            intraversal(self,root.left)
            ans.append(root.val)
            intraversal(self,root.right)
        
        intraversal(self,root)
        x = ans[:]
        ans.sort()
        d = defaultdict(int)
        for i in x:
            d[i]+=1
        flag = True
        for i in d.values():
            if i !=1:
                flag = False
        if x!= ans:
            flag = False
        return flag
        

