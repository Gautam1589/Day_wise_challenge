class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #approach-2
        carry,i=0,len(digits)-1
        while i>=0:
            n=digits[i]
            if i==len(digits)-1:
                n+=1+carry
            else:
                n+=carry
            if n>9:
                digits[i]=0
                carry=1
            else:
                digits[i]=n
                carry=0
            
            if carry==0:
                break
            i-=1
        
        if i==-1 and carry!=0:
            digits.insert(0,carry)
                
        return digits
        
        
        #approach-1
        s=''
        for i in digits:
            s+=str(i)
        n=int(s)
        n+=1
        s=str(n)
        digits=[]
        for i in range(len(s)):
            digits.append(int(s[i]))
        return digits
