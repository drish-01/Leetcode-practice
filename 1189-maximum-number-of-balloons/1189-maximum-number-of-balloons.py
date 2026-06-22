class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        countb=0
        counta=0
        countl=0
        counto=0
        countn=0
        for i in text:
            if i == 'b':
                countb+=1
            elif i == 'a':
                counta+=1
            elif i == 'l':
                countl+=1
            elif i == 'o':
                counto+=1
            elif i == 'n':
                countn+=1
            else:
                pass
        countl= countl//2
        counto=counto//2
        banlist = [countb, counta, countl, counto, countn]
        return min(banlist)
        