class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ansarr =[]
        sumtotal=0
        for i in range(len(nums)):
            sumtotal+=nums[i]
        subtractor=0
        for i in range(len(nums)):
            sumtotal-=nums[i]
            ansarr.append(sumtotal-subtractor)
            subtractor+=nums[i]

        for i in range(len(ansarr)):
            if ansarr[i]<0:
                ansarr[i]=-(ansarr[i])
        return ansarr