class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        n=len(list1)
        sumall=float('inf')
        name=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                if sumall > i + list2.index(list1[i]):
                    sumall = i + list2.index(list1[i])
                    name=[]
                    name.append(list1[i])
                elif sumall == i + list2.index(list1[i]):
                    name.append(list1[i])
            if i>sumall:
                break
        return name
        
        