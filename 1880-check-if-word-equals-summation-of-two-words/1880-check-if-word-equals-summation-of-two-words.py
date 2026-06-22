class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        lettonum = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
        firstWord = "".join(str(lettonum[i]) for i in firstWord)
        secondWord = "".join(str(lettonum[i]) for i in secondWord)
        targetWord = "".join(str(lettonum[i]) for i in targetWord)
        firstWord = int(firstWord)
        secondWord = int(secondWord)
        targetWord = int(targetWord)
        return targetWord == firstWord + secondWord