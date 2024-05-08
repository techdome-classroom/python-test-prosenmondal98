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
                if grid[i][j]=='L':
                    pass
                # left check
                if j==0:
                    continue
                # right check
                if j==c-1:
                    continue

                # bottom check
                if i==r-1:
                    continue

                    
        return 0