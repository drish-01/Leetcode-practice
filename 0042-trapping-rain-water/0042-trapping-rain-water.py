class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapped = 0 
        rightmax = 0 
        leftmax = 0 
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                leftmax = max(leftmax, height[left])
                trapped += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                trapped += rightmax - height[right]
                right -= 1

        return trapped