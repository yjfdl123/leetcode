class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        if length==0: return 0
        stack = []
        start,end = 0,length
        maximum=0
        while start<end:
            if stack==[] or heights[start]>=stack[-1]:
                stack.append( heights[start] )
            else:
                count = 0
                while stack and heights[start]<stack[-1]:
                    count+=1
                    maximum = max(maximum, stack.pop()*count )
                stack.extend( [heights[start]]*(count+1) )
            start+=1
        count=0
        while stack:
            count+=1
            maximum = max(maximum, stack.pop()*count)
        return maximum
so  = Solution()
print so.largestRectangleArea([3,10,3,4])






