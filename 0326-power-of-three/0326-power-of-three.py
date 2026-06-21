class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n<=0:
            return False
        while True:
            if n%3==0:
                n=n/3
            else:
                break
        if n==1:
            return True
        return False
        