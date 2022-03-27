class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
            
        res=[None]*len(nums)
        
        i,j=0,len(nums)-1
        for k in range(len(nums)-1,-1,-1):
            if nums[i]<nums[j]:
                res[k]=nums[j]
                j-=1
            else:
                res[k]=nums[i]
                i+=1
            
        return res
