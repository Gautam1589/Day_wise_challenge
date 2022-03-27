class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #hash map
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        n=len(nums)//2
        for i in d:
            if d[i]>n:
                return i
            
        #brute force
        c=1
        m=nums[0]
        for i in nums:
            if i==m:
                c+=1
            else:
                c-=1
            if c==0:
                m=i
                c=1
        return m
        
                    
