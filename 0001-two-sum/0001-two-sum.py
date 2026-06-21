class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for s in range(i+1, len(nums)):
                if nums[i]+nums[s] == target:
                    return [i, s]
        