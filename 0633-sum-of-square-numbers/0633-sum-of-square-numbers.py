class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        low = 0
        high = int(c**0.5) 
        
        while low <= high:
            if (low**2 + high**2) == c:
                return True
            elif (low**2 + high**2)< c:
                low+=1
            else:
                high-=1
        return False


        