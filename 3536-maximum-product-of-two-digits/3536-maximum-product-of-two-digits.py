class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        larg1= 0
        larg2=0
        temp = abs(n)
        while temp!=0:
            s = temp%10
            if s>larg1:
                larg2=larg1
                larg1 = s
            elif s>=larg2:
                larg2 = s
            temp = temp//10
        
        return larg1*larg2

        