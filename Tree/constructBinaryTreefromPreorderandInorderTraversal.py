# (105. Medium )Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Ex1 : 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Solution 1 : Recursive
# 1) The first element of the preorder array is always the root node.
# 2) Next to determine the left and right subtree, we can refer the inorder array.
# 3) We can find the root element in inorder array. The elements to the left of it will form left subtree and elements to right will form right subtree.
# 4) Recursively can call the algorithm and build the entire tree.

# Time : O(n^2), Space : O(n^2), because of the inorder.index() function and passing subarrays of preorder/inorder in each stack of the recursion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  # Base Case, when either arrays are exhausted
            return None
        root = TreeNode(preorder[0]) # Create the root node
        mid = inorder.index(preorder[0]) # Find the index of root element in inorder array
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root

# Solution 2 : Same as above but reducing the time and space to O(logn)
# Do one initial pass of the inorder array and create a hashmap of values to indexes, then each index lookup will be O(1). Also, instead of duplicating the arrays over and over again, just pass start and end indexes for each array. To keep things clean, create a surrounding class that can hold the arrays and the hashmap, then the function that does all the work can be an instance method that accesses these values nicely.
# This will reduce runtime complexity to O(n) and space complexity to O(logn)