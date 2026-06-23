class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=bin(n)[2:]
        t=len(p)
        newbin =0
        for i in p:
            if i =='0':
                newbin+=10**(t-1)
            t-=1
        newbin =str(newbin)
        return int(newbin, 2)
        