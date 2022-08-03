# (235. Easy) Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Ex 1 :
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Ex 2 :
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

# Solution 1 : O(n) time iterative
# Well-order property of BST, with unique elements ( given by description )
# all value on left sub-tree < value of current node < all value on right sub-tree

# Algorithm:
# Three possible cases:
# Case_#1:
# Both p and q are smaller than current node, then search left-subtree by recursive

# Case_#2:
# Both p and q are larger than current node, then search right-subtree by recursive

# Case_#3:
# Both p and q are not on the same side of current node, then current node must be the Lowest common ancestor of ( p, q )

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

# Solution 2 : Same as above, but recursive approach. Recursive stack will take up some space.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_value = root.val
        
        if p.val > cur_value and q.val > cur_value:
            return self.lowestCommonAncestor( root.right, p, q)
        
        elif p.val < cur_value and q.val < cur_value:
            return self.lowestCommonAncestor( root.left, p, q)
        
        else:
            return root

