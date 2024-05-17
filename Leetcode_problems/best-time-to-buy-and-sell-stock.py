class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for t in prices[1:]:
            if buy > t:
                buy=t
            profit = max(profit,t-buy)
        return profit
       
        