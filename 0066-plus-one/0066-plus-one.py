class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=0
        for i in range(len(digits)):
            s += digits[i] * (10**(len(digits)-i - 1))
        s += 1
        return [int(d) for d in str(s)]
