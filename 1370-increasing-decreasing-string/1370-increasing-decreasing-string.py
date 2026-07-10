class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r =sorted(s)
        output=""
        prev=""
        for i in r:
            if prev != i:
                output+=i
                s=s.replace(i, "", 1)
                prev=i
        if s=="":
            return output

        larg = "".join(sorted(s, reverse=True))
        prev = ""
        for i in larg:
            if prev != i:
                output+=i
                s=s.replace(i, "", 1)
                prev=i 
        if s == "":
            return output
        else:
             extra = self.sortString(s)
             output+=extra
             return output
             

        