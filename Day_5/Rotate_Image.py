class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n1=len(matrix)
        n2=len(matrix[0])
        for i in range(n1):
            for j in range(n2):
                if i<j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n1):
            j,k=0,n2-1
            while j<k:
                matrix[i][j],matrix[i][k]=matrix[i][k],matrix[i][j]
                j+=1
                k-=1
        return matrix
