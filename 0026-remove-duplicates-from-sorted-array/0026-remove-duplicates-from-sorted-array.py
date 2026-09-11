class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        mid = 0
         
        while mid < len(nums):
            if nums[low]==nums[mid]:
                mid+=1
                
            else:
                low+=1
                nums[low]= nums[mid]
                mid+=1
        return low + 1
        