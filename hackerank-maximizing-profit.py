    """
    
    HackerRank Challenge # 1
    
    """
    
    def maximumProfit(prices):
    # Write your code here
        idx = prices.index(max(prices))
        maxP = 0
        for i in range(len(prices)):
            if i < idx and prices[i] < max(prices):
                profit = max(prices) - prices[i]
                maxP += profit
                print(profit)
            
        if idx == len(prices) - 1:
            return maxP
        else: