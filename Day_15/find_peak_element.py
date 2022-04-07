class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        beg=0
        end=len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            else:
                if nums[mid]<nums[mid+1]:
                    beg=mid+1
                else:
                    end=mid-1
