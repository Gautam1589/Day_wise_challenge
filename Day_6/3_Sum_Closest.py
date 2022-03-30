class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m=sys.maxsize
        s=0
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            a=target-nums[i]
            j=i+1
            k=n-1
            while j<k:
                b=nums[j]+nums[k]
                d=abs(b-a)
                if d<m:
                    m=d
                    s=nums[i]+b 
                if b<a:
                    j+=1
                else:
                    k-=1
        return s
