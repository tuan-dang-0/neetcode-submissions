class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currBuy = prices[0]

        ret = 0

        for price in prices:
            ret = max(ret, price - currBuy)

            currBuy = min(currBuy, price)
        
        return ret
            