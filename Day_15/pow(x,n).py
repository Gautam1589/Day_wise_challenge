class Solution:
    def myPow(self, x: float, n: int) -> float:
        p=abs(n)
        res=1.0
        while p:
            if p&1:
                res*=x
            x*=x
            p>>=1
        
        if n>=0:
            return res
        else:
            return 1/res
