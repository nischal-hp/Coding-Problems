# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Ex: 
# For root level node, depth is 1.
# For second level nodes, depth becomes 2 and so on.
# If no tree exists, then depth is 0.

# Solution 1 : Iterative Approach :

# Can easily make out that this could be solved using BFS approach. We have to increment 
# the depth variable when we go to the next level . BFS can be implemented using queue approach.

def maxDepth(root):
    depth=0
    level= [root] if root else []  # Array holding the elements in each level
    while level:
        depth+=1
        queue=[]     # Refresh queue variable after each level
        for el in level:
            if el.left:
                queue.append(el.left)   # Pop elements into queue if they exist
            if el.right:
                queue.append(el.right)
        level=queue     # Go to the next level
    return depth 

# Solution 2 : Recursive Approach :

# We have to go on recursively exploring left and right subtrees, as long as they exist;
# and find out the max out of both of those . 

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left),maxDepth(root.right))+1

