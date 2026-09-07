class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxim= 0
        l = 0 
        r = len(height)-1
        
        while l<r:
            if height [l]<height[r]:
                maxim = max(maxim, (r-l)*height[l])
                l+=1       
            else:
                maxim = max(maxim, (r-l)*height[r])
                r-=1   
        return maxim