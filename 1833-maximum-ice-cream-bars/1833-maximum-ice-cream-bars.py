class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        count = 0
        tcost=0
        costs.sort()
        for i in costs:
            if i + tcost <=coins:
                count+=1
                tcost+=i
        return count