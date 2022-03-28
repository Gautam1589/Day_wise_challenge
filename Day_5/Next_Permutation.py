class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1. first find largest index k such that nums[k]<nums[k+1] 
        #else permutation is last permutation
        #2. find largest index l>k such that nums[j]>nums[k] and swap nums[l] and nums[k]
        #3. reverse from nums[k+1] upto last array
        
        for k in range(len(nums)-2,-1,-1):
            if nums[k]<nums[k+1]:
                break
        else:
            nums.sort()
            return nums
                
        for l in range(len(nums)-1,k,-1):
            if nums[l]>nums[k]:
                nums[l],nums[k]=nums[k],nums[l]
                break
                
        i,j=k+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
        return nums
