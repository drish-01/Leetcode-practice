class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
       
        mylist=letters + [target]
        mylist=set(mylist)
        mylist=list(mylist)
        mylist.sort()
        if target == mylist[len(mylist)-1]:
            return letters[0]
        for i in range(len(mylist)):
            if mylist[i]==target:
                return mylist[i+1]
        