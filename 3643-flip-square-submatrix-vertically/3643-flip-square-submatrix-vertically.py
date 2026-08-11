class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        i = x
        
        lastRind = x+k-1
        rownum=0
        
        while i <=x+(k-1)//2:
            j= y
            while j<=(y+k-1):
                temp = grid[i][j]
                grid[i][j]=grid[lastRind-rownum][j]
                grid[lastRind-rownum][j]=temp
                
                j+=1
            rownum+=1    
            i+=1
        
        return grid

                
        