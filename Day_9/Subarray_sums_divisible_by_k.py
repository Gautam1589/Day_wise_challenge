class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        c=[0]*(n+1)
        r=[0]*(n+1)
        f=[0]*k
        cnt=0
        
        #cumulative
        for i in range(1,n+1):
            c[i]=c[i-1]+nums[i-1]
        
        #remainder with k
        for i in range(n+1):
            r[i]=c[i]%k
            
        #calculate frequency
        for i in range(n+1):
            f[r[i]]+=1
            
        #calculate nof ways of all values
        for i in range(k):
            cnt+=(f[i]*(f[i]-1))//2
        return cnt
