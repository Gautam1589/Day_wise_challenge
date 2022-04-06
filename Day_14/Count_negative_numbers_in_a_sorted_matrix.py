class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        c,i,j=0,m-1,0
        while i>=0 and j<n:
            if grid[i][j]>=0:
                j+=1
            else:
                c+=n-j
                i-=1
        return c
