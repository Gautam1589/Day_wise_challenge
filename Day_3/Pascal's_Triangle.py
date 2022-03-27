class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        res.append([1])
        if numRows==1:
            return res
        res.append([1,1])
        if numRows==2:
            return res
        
        for i in range(2,numRows):
            l=res[-1]
            temp=[]
            temp.append(1)
            for i in range(len(l)-1):
                temp.append(l[i]+l[i+1])
            temp.append(1)
            res.append(temp)
        
        return res
        
