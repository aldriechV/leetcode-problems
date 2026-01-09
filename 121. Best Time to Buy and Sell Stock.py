"""
Docstring for 121. Best Time to Buy and Sell Stock
"""



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, currProfit)
            else:
                left = right
            right += 1

        
        return maxProfit