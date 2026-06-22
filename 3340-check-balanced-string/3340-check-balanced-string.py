class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        evensum = 0
        oddsum = 0
        oddcycle = True
        for i in num:
            i=int(i)
            if oddcycle == True:
                oddsum+=i
            else:
                evensum+=i
            oddcycle = not oddcycle

        if evensum == oddsum:
            return True
        return False