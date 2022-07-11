# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Ex 1 :
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Ex 2 :
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Ex 3 :
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Solution 1 : Iteratively BFS 
# We have to return the node of the cloned copy, which is like the root in LL. 
# Cloned copy means we have to create the Graph from first. 
# Turns out that maintaining a dictionary/hashmap that associates original node to its clone {node: clone_node} makes this process very simple. This hashmap also serves as a visited set to make sure you don't loop indefinitely while DFS/BFS.

# Time : O(E+V), where E - edges in graph, V - vertices. Space : O(V), for the dictionary

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
BFS - QUEUE
''' 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
         if not node: return  # Edge Case
         # map original nodes to their clones
         d = {node : Node(node.val)}
         q = deque([node])
        
         while q:
             for i in range(len(q)):  # Since it is BFS, have to iterate through the entire queue
                 currNode = q.popleft()
                 for nei in currNode.neighbors:
                     if nei not in d:  # This has to be checked first, so that the node can be created before adding it as a neighbor
                         # store copy of the neighboring node
                         d[nei] = Node(nei.val)
                         q.append(nei)
                     # connect the node copy at hand to its neighboring nodes (also copies) -------- [1]
                     d[currNode].neighbors.append(d[nei])
        
         # return copy of the starting node ------- [2]
         return d[node]

# Solution 2 : Iteratively DFS
# Same as above soln, but using DFS instead

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        d = {node: Node(node.val)}
        stack = [node]
        while stack:
            curNode = stack.pop()
            for nei in curNode.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    stack.append(nei)
                d[nei].neighbors.append(d[curNode])
        return d[node] # return the value of the original node which is a copy of that original node

# Solution 3 : Recursively DFS, without using any stack/queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew={}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy=Node(node.val)
            oldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
            
        return dfs(node) if node else None # Edge case where node can be None
