class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        r, c=len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='W':
                    continue
                #  top check
                if i==0:
                    continue
                elif grid[i][j]=='L'
                # left check
                elif j==0:
                    continue
                # right check
                elif j==c-1:
                    continue
                # bottom check
                elif i==r-1:
                    continue

                    
        return 0