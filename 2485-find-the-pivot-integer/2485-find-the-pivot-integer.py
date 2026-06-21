class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = n * (n + 1) // 2
        for x in range (1,n+1):
            sumtillx = x * (x+1)//2
            sumx2n = total_sum + x - sumtillx 
            if (sumtillx == sumx2n):
                return x
        return -1