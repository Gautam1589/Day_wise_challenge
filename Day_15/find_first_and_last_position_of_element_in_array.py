class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        beg,flag1=0,0
        end=len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target and (nums[mid-1]<target or mid==0):
                flag1=1
                break
            else:
                if nums[mid]<target:
                    beg=mid+1
                else:
                    end=mid-1
        if flag1==1:
            l.append(mid) 
        else:
            l.append(-1)
            
        beg,flag2=0,0
        end=len(nums)-1
        while beg<=end:
            mid=(beg+end)//2
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]>target):
                flag2=1
                break
            else:
                if nums[mid]<=target:
                    beg=mid+1
                else:
                    end=mid-1
        if flag2==1:
            l.append(mid)
        else:
            l.append(-1)
        return l
