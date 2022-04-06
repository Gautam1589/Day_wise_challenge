class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        
        def NSER():
            l=[0]*n
            s=[]
            for i in range(n-1,-1,-1):
                while len(s)!=0 and s[-1][0]>=heights[i]:
                    s.pop()
                if len(s)==0:
                    l[i]=n
                else:
                    l[i]=s[-1][1]
                s.append([heights[i],i])
            return l
        def NSEL():
            s=[]
            l=[0]*n
            for i in range(0,n):
                while len(s)!=0 and s[-1][0]>=heights[i]:
                    s.pop()
                if len(s)==0:
                    l[i]=-1
                else:
                    l[i]=s[-1][1]
                s.append([heights[i],i])
            return l
        l1=NSER()
        l2=NSEL()
        maxarea=0
        for i in range(len(l1)):
            maxarea=max((l1[i]-l2[i]-1)*heights[i],maxarea)
        return maxarea
