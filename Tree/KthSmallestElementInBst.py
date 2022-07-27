# (230. Medium) Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Ex 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Ex 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Solution 1 : Iterate through BST and use an array to store values. O(nlogn) time, O(n) space
# Iterate through BST and use an array to store the values.
# Sort the values and return based on k-value

class Solution:
    # O(nlogn) time,O(n) space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values=[]
        def traverseBST(root):
            if root:
                values.append(root.val)
            if root.left:
                traverseBST(root.left)
            if root.right:
                traverseBST(root.right)
        traverseBST(root)
        return sorted(values)[k-1]

# Solution 2 : O(n) time and space. In-order traversal
# We know that in-order traversal has the elements in the sorted order. So we can use this property to solve the problem by modifying above solution.

# Recursively : 

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]

# Solution 3 : Iterative inorder traversal using k as the reference. O(n+k) time,O(n) space
# We keep a stack. We go on iteratively visiting the left subtree.
# We continue until we encounter a leaf node.
# At this point we are at the smallest element in the tree. Hence we have to pop an element from stack.
# It also means, if k=1, we have found our smallest element. So use another variable to keep track of when we meet k.
# Once a value is popped out of stack, we then have to go on visiting the right subtree.

# Time complexity: O(H + k), where H is a tree height. This complexity is defined by the stack, which contains at least H + k elements, since before starting to pop out one has to go down to a leaf. This results in O(logN+k) for the balanced tree and O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
# Space complexity: O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of the skewed tree, and O(logN) in the average case of the balanced tree.
class Solution:
    # O(n+k) time,O(n) space - Iterative inorder traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stack=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()   # Have encountered a leaf node, in left subtree
            n+=1
            if n==k:
                return cur.val
            cur = cur.right   # Move to the right subtree

# Solution to Follow up Question : 
# The time complexity for insert/delete operations is O(H), where H is a height of the binary tree. H =logN for the balanced tree and H =N for a skewed tree.
# Hence without any optimisation insert/delete + search of kth element has O(2H + k) complexity. How to optimise that?

# That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :
# Insert
# Delete
# Find kth smallest

# Let's use here the same logic as for LRU cache design, and combine an indexing structure (we could keep BST here) with a double linked list.
# Such a structure would provide:
# O(H) time for the insert and delete.
# O(k) for the search of kth smallest.

# The overall time complexity for insert/delete + search of kth smallest is O(H + k) instead of O(2H + k).

# Complexity Analysis
# Time complexity for insert/delete + search of kth smallest: O(H+k), where H is a tree height. O(logN+k) in the average case, O(N+k) in the worst case.
# Space complexity : O(N) to keep the linked list.