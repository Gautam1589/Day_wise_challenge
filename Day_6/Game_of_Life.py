class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirn=[[0,1],[1,0],[1,1],[-1,-1],[0,-1],[-1,0],[1,-1],[-1,1]]
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            for j in range(n):
                cnt=0
                for k in dirn:
                    I=i+k[0]
                    J=j+k[1]
                    if I<0 or I>=m or J<0 or J>=n:
                        continue
                    if board[I][J]==1 or board[I][J]==2:
                        cnt+=1
                #print(cnt)
                if (board[i][j]==1 or board[i][j]==2) and (cnt<2 or cnt>3):
                    board[i][j]=2
                elif board[i][j]==0 and cnt==3:
                    board[i][j]=3
                #print(board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=0
                elif board[i][j]==3:
                    board[i][j]=1
        
        return board
