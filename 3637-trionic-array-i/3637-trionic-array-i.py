class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p=0
        
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                p+=1
            elif nums[i]>nums[i+1]:
                break
            else:
                return False
        if p == len(nums)-1:
            return False
        q=p
        for i in range(p, len(nums)-1):
            if nums[i]>nums[i+1]:
                q+=1
            elif nums[i]<nums[i+1]:
                break
            else:
                return False 
        if q == len(nums)-1:
            return False
        n=q
        for i in range(q, len(nums)-1):
            if nums[i] <nums[i+1]:
                n+=1
            else:
                return False
        
        if 0< p< q< n:
            return True
        return False 
        