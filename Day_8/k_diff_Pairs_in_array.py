class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            
        s=set()

        for i in nums:
            if i==k+i:
                if d[i]>1:
                    s.add((i,k+i))
            elif k+i in d:
                s.add((i,k+i))
                
                
        return len(s)
