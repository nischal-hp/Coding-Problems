# (269 .Hard) There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:

# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# Example 2:

# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:

# Input:
# [
#   "z",
#   "x",
#   "z"
# ]

# Output: "" 

# Explanation: The order is invalid, so return "".

# Constraints:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# Solution : Topological sort using Post Order DFS on a DAG. O(length of words array*unique characters) time ,O(unique characters in words) space.
# Basically, we check for 2 words at a time. When we encounter the first char which is diff, then we can get to know the ordering.
# Ex : abc, abd are first 2 words. ab is common, so it would be sorted on the last char. So can assume c comes before d, and build a graph out of it c->d.
# Like this, we take 2 words at a time and iterate through the list.
# In case if we encounter a cycle in the list, that means the words are contradicting each other, as order can be anything in a cycle. So in that case return ""
# Another case is if 1st word is a prefix of the 2nd word (i.e length of 1st word > length of 2nd word, and entire 1st word is contained within 2nd word).

# We need to have a visited variable which keeps track of whether the node is in the current path, to identify if there is a cycle.
# The other thing we need to do, is to do post order traversal while doing DFS. Coz in the case of, a->b->c, and another loop a->c. If we do normal DFS, the order we get is ACB.
# If we do post order DFS, we have to go till the leaf node first. Hence, first we encounter c. Next we come back to a, and go to b. Lastly we visit a.
# Thus order we get is "cba", which is result in reverse order. Hence, we just have to reverse it before using it.

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True : visited and in current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)