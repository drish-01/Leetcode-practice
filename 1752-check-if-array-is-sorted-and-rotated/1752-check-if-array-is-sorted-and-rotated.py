class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newlist = []
        sortedarray = sorted(nums)
        if sortedarray == nums:
            return True
        n = len(nums)
        
             
        if nums[0] < nums[n-1]:
                return False
        count = 0
        for i in range(n-1):
            if nums[i] <= (nums[i+1]):
                pass
            else:
                count=i+1
                break
        
        for t in range(count, len(nums)):
            newlist.append(nums[t])
        for s in range(0, count):
            newlist.append(nums[s])
        if newlist == sortedarray:
            return True
        return False
        