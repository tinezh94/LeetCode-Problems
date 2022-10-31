"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfit(prices):
    # two-pointer
    left, right = 0, 1
    maxProfit = 0
    # while the right index is less than the length of prices
    while right < len(prices):
        # if prices at left index is less than the price at right index, the profit is the difference
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            # compare profit with the max profit
            maxProfit = max(profit, maxProfit)
        else:
            # if the price at left index is greater than the price at right index, then it's not the lowest buying point, so shift the left pointer to the right pointer
            left = right
        # always shift the right pointer to the next index to compare with the lowest buying point to get the max profit
        right = right + 1
    
    return maxProfit



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))