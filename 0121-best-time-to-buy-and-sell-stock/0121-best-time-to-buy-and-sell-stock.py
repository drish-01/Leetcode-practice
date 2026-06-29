class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice=float("inf")
        profit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > profit:
                profit = price - minprice
        return profit