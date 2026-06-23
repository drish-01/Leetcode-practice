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
            ansarr.append(abs(sumtotal-subtractor))
            subtractor+=nums[i]

        
        return ansarr