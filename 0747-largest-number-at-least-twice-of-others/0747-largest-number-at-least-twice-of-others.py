class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newnum =sorted(nums)
        lastind=len(newnum)-1
        if (newnum[lastind])<(2*newnum[lastind-1]):
            return -1
        largest=newnum[lastind]
        for i in range(len(nums)):
            if nums[i]==largest:
                return i 
