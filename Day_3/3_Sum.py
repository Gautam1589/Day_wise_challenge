class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        l=[]
        d={}
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                res=nums[i]+nums[j]+nums[k]
                if res==0:
                    if res not in d:
                        d[(nums[i],nums[j],nums[k])]=1
                if res>0:
                    k-=1
                else:
                    j+=1
                    
        for i in d:
            l.append(list(i))
        #print(l)
        return l
