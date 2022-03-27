class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Kadane's algo
        currsum=0
        res=0
        for i in range(len(prices)-1):
            currsum+=prices[i+1]-prices[i]
            if currsum<0:
                currsum=0
            res=max(res,currsum)
            
        return res
        
