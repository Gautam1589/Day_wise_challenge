class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(nlogn)
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            if self.binary_search2(matrix,target,i,n):
                return True
        return False
              
    def binary_search2(self,matrix,target,row,n):
        beg,end=0,n-1
    
        while beg<=end:
            mid=(beg+end)//2
            if matrix[row][mid]==target:
                return True
            else:
                if matrix[row][mid]<target:
                    beg=mid+1
                else:
                    end=mid-1
                    
        return False
