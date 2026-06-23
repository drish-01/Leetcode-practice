class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=bin(n)[2:]
        
        newbin =''
        for i in p:
            if i =='0':
                newbin+="1"
            else:
                newbin+="0"
        
        return int(newbin, 2)
        