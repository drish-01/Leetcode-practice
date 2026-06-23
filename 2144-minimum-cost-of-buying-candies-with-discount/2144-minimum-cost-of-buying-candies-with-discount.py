class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<3:
            return sum(cost)
        cost.sort(reverse=True)
        n=1
        totalcost=0
        for i in range(len(cost)):
            if n%3==0:
                n+=1
                continue
            totalcost+=cost[i]
            n+=1
        return totalcost

        