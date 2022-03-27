class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        i=0
        intervals.sort(key=lambda x:x[0])
        while i<len(intervals):
            start=intervals[i][0]
            end=intervals[i][1]
            while i+1<len(intervals) and end>=intervals[i+1][0] and start<=intervals[i+1][1]:
                start=min(start,intervals[i+1][0])
                end=max(end,intervals[i+1][1])
                i+=1
            
            l.append([start,end])
            i+=1
        return l
