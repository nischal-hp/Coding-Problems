# (431. Medium) ind the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

# Ex : Input : n=5, edges = [[0,1],[1,2],[3,4]]
# Output : 2

# Solution : O(E+V) time and space. Using adjacency list and DFS
# First build adjacency list to find the list of neighbors for each vertex.
# Then do dfs for each variable in range(n). Mark the visited vertices.
# If a vertex is already visited, dont do DFS again.
# Each time DFS function is called, means we have found a new connected component. Hence increment the result by 1.

def components(n,edges):
    res = 0
    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    visit = set()
    def dfs(val):
        if val in visit:
            return False
        visit.add(val)
        for neigh in adj[val]:
            dfs(neigh)
        return True

    for i in range(n):
        if i not in visit:
            dfs(i)
            res+=1
    return res
    
print(components(5,[[0,1],[2,3]]))
