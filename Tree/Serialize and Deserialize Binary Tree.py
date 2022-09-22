# (297. Hard) Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Ex 1 :
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000

# Solution 1 : Using Pre-Order traversal and DFS
# For encoding, we traverse the binary tree in a pre-order traversal method. If Null value is found, we append 'X' to the result.
# The values are stored in an array which is later combined to form a string separated by ','

# For decoding, we first split the string using ',' as delimiter
# We use a index variable, self.i; which keeps track of the position in the array
# If we find a value of 'X', we return None.
# We construct the tree back, node-by-node; and then return the root node finally.
 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(node):
            if not node:
                res.append('X')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals=data.split(',')
        self.i=0
        def dfs():
            if vals[self.i]=='X':
                self.i+=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()