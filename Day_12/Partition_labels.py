class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #vis={}
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
            
        d={}
        res=[]
        l=1
        curr_freq=freq[s[0]]
        d[s[0]]=1
        
        for i in s[1:]:
            if curr_freq!=l:
                l+=1
                if i not in d:
                    d[i]=1
                    curr_freq+=freq[i]
            else:
                res.append(l)
                l=1
                d[i]=1
                curr_freq=freq[i]
            #print(l,curr_freq,res)
            
        
        if len(s)==1:
            res.append(len(s))
        else:
            res.append(l)
        return res
