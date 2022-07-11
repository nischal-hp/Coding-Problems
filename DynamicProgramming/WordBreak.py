# (139. Medium) Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
 
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Solution 1 : O(n^2). 
# Start from each char in s, form a substring from s till the length of string, and check if the word can be found in the wordDict or not.
# Repeat this starting from each char.
# Then finally find out if the entire word can be formed from words in wordDict or not.


# Solution 2 DP : Time O(n.m.n), m- len of wordDict, n - len of s. The final n comes from the check where we see, if substring matches the word.
# Space : O(n)
# We start with each of the words in wordDict, then check if any of those matches with starting part of the string.
# If it does, then we move onto the remaining part of the string, and repeat the process there.

# Decision Tree:
# Ex Input: s = "leetcode", wordDict = ["leet","code"]
# We keep track of index. Start from i=0. From here we can do 2 checks. Check if leet and code can be formed from the substring.
# If any of those are true, repeat the step for the remaining part of s.
# Finally if we are at the end of string, and we get True for any of the matches, overall result is True.

# Cache:
# The result can be cached, so as not to repeat the process again.

# Code : Bottom up approach
# Start from the end of string. Initialize the value outside the string to be equal to True.

class Solution:
    # DP solution, O(n.m.n), Space : O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp= [False] * (len(s)+1)
        dp[len(s)] = True  # Base Case
        for i in range(len(s)-1,-1,-1):  # Traverse in Reverse Order
            for word in wordDict:
                if s[i:i+len(word)]==word and i+len(word)<=len(s):  # Check if it matches with word, and also if there are enough characters in word to make the comparision. Second condition maybe optional
                    dp[i] = dp[i+len(word)]
                if dp[i]:   # If its already True, we dont need to check with other words in dictionary, hence break
                    break
        return dp[0]

# Solution 3 : Using BFS/DFS

# Starts with string s. For each string visited, chop off front of string if it starts with a word in the dictionary and adds the shortened string to the queue or stack. If string becomes empty, that means word break succeeded. Keep a set of seen string states to avoid duplicate work.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
   		q = deque([s])
		seen = set() 
		while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
					if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False