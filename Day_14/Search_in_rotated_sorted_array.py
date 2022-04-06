class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg,n=0,len(nums)
        end=n-1
        flag=0
        while(beg<=end):
            mid=(beg+end)//2
            if (mid==n-1 or nums[mid]>nums[mid+1]) and (mid==0 or nums[mid]>nums[mid-1]):
                flag=1
                break
            else:
                if nums[mid]>nums[-1]:
                    beg=mid+1
                else:
                    end=mid-1
        if flag==1:
            if nums[mid]==target:
                return mid
            elif nums[0]<=target:
                beg=0
                end=mid
            else:
                beg=mid+1
                end=n-1
        else:
            beg=0
            end=n-1
        flag=0
        while(beg<=end):
            mid=(beg+end)//2
            if nums[mid]==target:
                flag=1
                break
            else:
                if nums[mid]<target:
                    beg=mid+1
                else:
                    end=mid-1
        if flag==1:
            return mid
        else:
            return -1
        
