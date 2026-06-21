class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n==2:
            return True
        n=float(n)
        if n<=0:
            return False
        while True:
            n = n / 2
            if n%2==0:
                if n == 2:
                    return True
                else:
                    pass
            else:
                return False
        
        return False
        