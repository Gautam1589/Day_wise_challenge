class Solution:
    global cnt, r, c
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.r=len(grid)
        self.c=len(grid[0])
        vis=[[False for i in range(self.c)] for j in range(self.r)]
        max_area=0
        for i in range(self.r):
            for j in range(self.c):
                self.cnt=0
                if grid[i][j]==1 and vis[i][j]==False:
                    #self.dfs(vis,i,j,grid)
                    self.bfs(vis,i,j,grid)
                    max_area=max(max_area,self.cnt)
                    
        return max_area
    
    def dfs(self,vis,i,j,grid):
        vis[i][j]=True
        self.cnt+=1
        
        if i-1>=0 and grid[i-1][j]==1 and vis[i-1][j]==False:
            #vis[i-1][j]=True
            self.dfs(vis,i-1,j,grid)
        if i+1<self.r and grid[i+1][j]==1 and vis[i+1][j]==False:
            #vis[i+1][j]=True
            self.dfs(vis,i+1,j,grid)
        if j-1>=0 and grid[i][j-1]==1 and vis[i][j-1]==False:
            #vis[i][j-1]=True
            self.dfs(vis,i,j-1,grid)
        if j+1<self.c and grid[i][j+1]==1 and vis[i][j+1]==False:
            #vis[i][j+1]=True
            self.dfs(vis,i,j+1,grid)
        
    def bfs(self,vis,i,j,grid):
        queue=[]
        queue.append((i,j))
        vis[i][j]=True
        self.cnt+=1
        while queue:
            i,j=queue.pop()
            
            if i-1>=0 and grid[i-1][j]==1 and vis[i-1][j]==False:
                vis[i-1][j]=True
                queue.append((i-1,j))
                self.cnt+=1
            if i+1<self.r and grid[i+1][j]==1 and vis[i+1][j]==False:
                vis[i+1][j]=True
                queue.append((i+1,j))
                self.cnt+=1
            if j-1>=0 and grid[i][j-1]==1 and vis[i][j-1]==False:
                vis[i][j-1]=True
                queue.append((i,j-1))
                self.cnt+=1
            if j+1<self.c and grid[i][j+1]==1 and vis[i][j+1]==False:
                vis[i][j+1]=True
                queue.append((i,j+1))
                self.cnt+=1
        
