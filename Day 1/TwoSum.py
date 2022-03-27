class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Approach 1: O(N) time
        d={}
        
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[target-nums[i]]=i
        
        #Approach 2: O(n^2) time
        i=0
        j=len(nums)-1
        l=[]
        l1=list(nums)
        nums.sort()
        while i<j:
            if nums[i]+nums[j]==target:
                l.append(l1.index(nums[i]))
                if l1.index(nums[j])==l[0]:
                    l1.pop(l1.index(nums[i]))
                    l.append(l1.index(nums[j])+1)
                else:
                    l.append(l1.index(nums[j]))
                return l
            else:
                if nums[i]+nums[j]>target:
                    j-=1
                else:
                    i+=1
