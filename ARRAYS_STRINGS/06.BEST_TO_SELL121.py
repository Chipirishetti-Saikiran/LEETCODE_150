#BRUTE FORCE 
class Solution(object):
    def maxProfit(self, prices):
        max_p = []
        for i in range(len(prices)):
            for j in range(i):
                if prices[i] > prices[j]:
                    max_p.append(prices[i] - prices[j])
        return max(max_p) if max_p else 0


#OPTIMAL 
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
                
        return max_profit