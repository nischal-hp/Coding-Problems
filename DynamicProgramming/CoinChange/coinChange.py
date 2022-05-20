# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Solution 1 : Greedy approach (Does not work)

# Suppose we start with the highest coin denomination. Go on adding it until the amount exceeds the target value.
# If it exceeds choose a smaller denomination and continue the process.
# But this does not always return the smallest denomination.
# Ex: [1,3,4,5], amount = 7.
# Start with 5. 5+5 exceeds 7, so go on decrementing value from 5.
# 5+4 > 7. 5+3 >7.
# But 5+1 < 7.
# Repeat the process again with 5+1.
# 5+1+3 or 5+1+4 > 7.
# But 5+1+1 = 7. But 3 is not the smallest no of coins.
# The soln is actually 2 (which is 4+3).
# So Greedy approach does not work.
# Can then start with 4, and repeat the same process. But its too complicated approach.


# Solution 2 : Brute Force/Dynamic Programming - (DFS+Backtracking) (Top Down+ Memoization)

# We create a decision tree where 
# from each denomiation, all other denominations are possible.
# Ex: [1,3,4,5]. target = 7.
# From 5, can again choose either 1,3,4,5. We go on doing this until the remainder = 0, which is our solution.
# Then backtrack to find out how many coins were used.
# If remainder exceeds amount, that means thats not our solution.
# Repeat the above process for all possible combinations and find out the minimum out of all.
# We can use memoization to reduce the process a bit. For Ex: If the remainder is 1, then we know that 
# we have to choose another 1 coin to get to the final result. Choosing any other coin will make us go over the 
# target. Hence can use this knowledge by storing it in a cache/dictionary.

from math import remainder


class Solution:
    def coinChange(self,coins,amount):
        memo = {}  # Dictionary used for memoization
        result = self.dfs(coins,amount,memo) # Call dfs on it
        if result==float('inf'):
            return -1
        return result
    
    def dfs(self,coins,amount,memo):
        if amount ==0:  # Which means we have reached the target value
            return 0
        if amount in memo:  # Use memoization table to not compute the values which we already know
            return memo[amount]
        minim = float('inf')  # Variable to keep track of the minimum value
        for c in coins:  # From each step, we can consider all the different coins
            remainder = amount-c  
            if remainder>=0:    # If remainder is negative, means we have alreadyx exceeded the target value
                minim = min(minim,self.dfs(coins,remainder,memo)+1)  # Make sure to add +1, to indicate that we have selected a coin
        memo[amount] = minim  # Add minim amount to dictionary
        return minim   # Return the value finally

# Solution 3 : DP. (Bottom-Up + Memoization)
# Here we start from the smallest value which is 0, and go all the way till amount;
# computing the smallest number of coins at each step.
# dp[0] = 0
# dp[1] = 1. Here check the input array [1,3,4,5]. 1 is minimum number of coins required to achieve target. Rest all exceed it.
# dp[2] = 1+dp[1]. Here 1 coin is chosen from [1,3,4,5], of value =1. And then used the prev. computed value for dp[amount-coin value chosen]
# Repeat above step for diff coins, and chose the minimum value out of it. 
# Compute until dp[7] and return it. 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}  # Dictionary used for memoization
        memo[0]=0  # Minimum number of coins used to get to amount = 0
        for i in range(1,amount+1):  # Have to go on till memo[amount], hence do amount+1
            minim=float('inf')
            for c in coins:
                rem = i - c
                if rem>=0:
                    minim=min(minim,1+memo[rem])  # Add 1 here, to indicate that we have chosen a coin
            memo[i]= minim           # Finally add it to Dictionary
        return memo[amount] if memo[amount]!=float('inf') else -1  # Finally return memo[amount]

