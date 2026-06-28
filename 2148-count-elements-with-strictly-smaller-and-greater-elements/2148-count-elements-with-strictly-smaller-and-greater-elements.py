class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        smallest = nums[0]
        largest = nums[len(nums)-1]
        count = len(nums) 
        for i in nums:
            if i == smallest or i==largest:
                count-=1
        return count
        