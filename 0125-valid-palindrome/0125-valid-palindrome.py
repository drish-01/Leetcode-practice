class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ""
        for i in s:
            if i.isalpha() == True or i.isdigit()==True:
                string = string + i
        string = string.lower()
        revstr= string[::-1]
        if string == revstr:
            return True
        return False
            
        