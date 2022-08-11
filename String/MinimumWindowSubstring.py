# (76. Hard) Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.

# Solution 1 : Brute Force : O(s^2) time,O(t) space. (TLE error)
# Have a dictionary which contains the count of char in t string.
# Iterate through s. If that char is in t, then call a function which iterates through the rest of the string.
# While iterating, if the char if found in dic, decrement it.
# At the end check if all values are 0 or not. 
# If all values are 0, its a valid substring.
# Return the minimum of such a substring.

class Solution:
    # Brute Force : O(s^2) time,O(t) space
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        minWindow=[]
        res=''
        def repopulate():
            dic = {}
            for i in range(len(t)):
                dic[t[i]] = 1 + dic.get(t[i],0)
            return dic

        
        def windowString(r):
            l=r
            while r<len(s):
                if s[r] in dic:
                    dic[s[r]] -=1
                if max(dic.values())==0:
                    return s[l:r+1]
                r+=1
            return ''
                
        dic = repopulate()

        for r in range(len(s)):
            if s[r] in dic:
                minWindow.append(windowString(r))
                dic = repopulate()

        for each in minWindow:
            if each!='':
                if res=='':
                    res=each
                else:
                    if len(each)<len(res):
                        res = each
        return res

# Solution 2 : O(s+t) time, O(s+t) space
    
# Keep t_counter of char counts in t

# We make a sliding window across s, tracking the char counts in s_counter
# We keep track of matches, the number of chars with matching counts in s_counter and t_counter
# Increment or decrement matches based on how the sliding window changes
# When matches == len(t_counter.keys()), we have a valid window. Update the answer accordingly

# How we slide the window:
# Extend when matches < chars, because we can only get a valid window by adding more.
# Contract when matches == chars, because we could possibly do better than the current window.

# How we update matches:
# This only applies if t_counter[x] > 0.
# If s_counter[x] is increased to match t_counter[x], matches += 1
# If s_counter[x] is increased to be more than t_counter[x], do nothing
# If s_counter[x] is decreased to be t_counter[x] - 1, matches -= 1
# If s_counter[x] is decreased to be less than t_counter[x] - 1, do nothing

# Analysis:
# O(s + t) time: O(t) to build t_counter, then O(s) to move our sliding window across s. Each index is only visited twice.
# O(s + t) space: O(t) space for t_counter and O(s) space for s_counter
    

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        if not s or not t or len(s) < len(t):
            return ''
        
        t_counter = Counter(t)
        chars = len(t_counter.keys())
        
        s_counter = Counter()
        matches = 0
        
        answer = ''
        
        i = 0 # This is left pointer 
        j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase. This is right pointer.
        
        while i < len(s):
            
            # extend
            if matches < chars:
                
                # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
                if j == len(s) - 1:
                    return answer
                
                j += 1
                s_counter[s[j]] += 1
                if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]: # The char should exist in t_counter and with value > 0
                    matches += 1

            # contract
            else:
                s_counter[s[i]] -= 1
                if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                    matches -= 1
                i += 1
                
            # update answer
            if matches == chars:
                if not answer:
                    answer = s[i:j+1]
                elif (j - i + 1) < len(answer):
                    answer = s[i:j+1]
        
        return answer