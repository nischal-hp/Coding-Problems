# (178. Medium) Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example
# Example 1:

# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.
# Example 2:

# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


# Solution : O(E+V) time and space (due to adjacency list and recursion)- Finding cycle in an undirected graph
# A tree is connected and has no cycles/loops in it. This is the difference when compared with a graph.
# For the soln, we first have to build an adjacency list. That is list of neighbors for each vertex.
# Next we have to start iterating from the starting vertex using DFS.
# We keep a track of all the visited nodes. In the end if no of visited nodes==n, that means the graph is connected and its a valid tree.
# To find any cycle inside the tree, we basically have to keep track of the prev node (Since its an undirected graph and an edge exists both ways in adjacency list).
# If an element is in visited set, and it is not the prev value, then we have detected a cycle, and can return False.
# Base Case is, if no neighbors are left to be visited, then can return True.

# Problem is free on Lintcode
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:    # Base Case - where a loop can exist
                return False

            visit.add(i)    # Add it to visit set. No need of removing from visit set
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):  # If it returns false, immideately return False
                    return False
            return True    # If not, then return True

        return dfs(0, -1) and n == len(visit)
