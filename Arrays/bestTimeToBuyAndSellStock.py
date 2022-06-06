# Array Problem

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Ex: 1) 
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Ex: 2) 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#### SOLUTION ####: 

# It is basically like a sorted array, since we have to buy the stock first before selling.
# SO we can go for 2 pointer approach to traverse the array similar to TwoSum problem.
# It is a Sliding Window Concept/ Kadane's Algorithm

# Some body might think that we can find min and max number from the array so that we can get the max profit. But here is one catch
# For Example:
# prices=[3,4,1,6]
# min=1
# max=6
# profit=max-min=5 which is correct 
# in this Example:
# prices = [7,6,4,3,1]
# min = 1 price at day 6
# max = 7 price at day 1
# max_profit = 7-1 = 6 u can think like this but you cant buy the stock at day 6 and sell it at day 1.


# Explanation:
# let use initialize Left and Right pointer to first and second position of array
# Here Left is to buy stock and Right is to sell stock

#     Then we initialize our max_profit as 0

#     Now we will start our while loop and we will run till our Right pointer less then length of array
#     For Example:

#     prices=[7,1,5,3,6,4]
#    Note:
#         prices[left] --> buy stock
#         prices[right] --> sell stock
#     now we will check price at right and left pointer
#     step 1:
#     price[left]=7 price[right]=1 profit=-6
# here price[left] is greater than price[right] so we will move left pointer to the right position and increment our right pointer by 1. We always want our left point to be minimum
#     step 2:
#     price[left]=1 price[right]=5 profit=4
#     here price[left] is less than price[right] which means we will get profit so we will update our max_profit and move our right pointer alone
#     step 3:
#     price[left]=1 price[right]=3 profit=2
#     here price[left] is less than price[right] which means we will get profit so we will check our max_profit previously it was 4 now our current profit is 2 so we will check which is maximum and update our max_profit and move our right pointer alone
#     step 4:
#     price[left]=1 price[right]=6 profit=5
#     here price[left] is less than price[right] which means we will get profit so we will check our max_profit previously it was 4 now our current profit is 5 so we will check which is maximum and update our max_profit and move our right pointer alone
#     step 5:
#     price[left]=1 price[right]=4 profit=3
#     same logic as above
# 	Big O :
# n--> length of array
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self,prices):
        left =0
        right=1
        max_profit = 0
        curr_profit = 0
        if len(prices)<2:
            return max_profit
        while right < len(prices):  # Traverse the entire array
            curr_profit = prices[right] - prices[left]
            if prices[right]>prices[left]:     # Make sure we can buy the stock before selling it
                max_profit = max(max_profit,curr_profit)
            else:
                left=right # It is not left+=1. It is left=right. Since it is sliding window algo.
            right+=1 # Go on incrementing right pointer every stage
        return max_profit


# Another Solution : 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, profit = float('inf'), 0   
        for price in prices:
            buy_price = min(price,buy_price)     
            profit = max(price - buy_price,profit)    
        return profit 
