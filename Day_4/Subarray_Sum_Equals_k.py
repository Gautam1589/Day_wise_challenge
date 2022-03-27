class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        nums.insert(0,0)
        
        #cumulative sum
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        #0 1 1 1 -> 0 1 2 3
        #pairs 0-2 1-3
        cnt=0
        for i in  nums:
            if i-k in d:
                cnt+=d[i-k]
            d[i]=d.get(i,0)+1
        #print(d)   
        return cnt
        
