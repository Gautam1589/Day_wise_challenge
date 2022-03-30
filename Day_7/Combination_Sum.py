class Solution:
    global res
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.backtrack(candidates,[],target)
        return self.res
    
    def backtrack(self,arr,subset,target):
        if target==0:
            self.res.append(subset[:])
            return
            
        if target<0:
            return
        
        for i in range(len(arr)):
            subset.append(arr[i])
            self.backtrack(arr[i:],subset,target-arr[i])
            subset.pop()
            
        return
