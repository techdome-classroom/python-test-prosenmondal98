class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        r, c=len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                #  top check
                if i==0:
                    continue
                
                # left check
                if j==0:
                    pass
                # right check
                if j==c-1:
                    pass
                # bottom check
                if i==r-1:
                    pass

                    
        return 0