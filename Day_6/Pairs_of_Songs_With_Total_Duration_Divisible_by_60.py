class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq=[0]*60
        
        for i in time:
            freq[i%60]+=1
            
        pairs=0
        pairs+=(freq[0]*(freq[0]-1))//2
        pairs+=(freq[30]*(freq[30]-1))//2
        
        i,j=1,59
        while i<j:
            if freq[i]!=0 and freq[j]!=0:
                pairs+=freq[i]*freq[j]
            i+=1
            j-=1
        
        return pairs
