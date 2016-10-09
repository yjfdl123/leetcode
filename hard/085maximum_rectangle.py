class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0 : return 0
        height = len(matrix)
        width  = len(matrix[0])
        histogram = [0]*width
        hei = 0
        maximum = 0
        while hei<height:
        	for wei in range(width):
        		# print matrix[hei][wei]
        		if matrix[hei][wei]=='1':
        			histogram[wei] = histogram[wei]+1
        		else:
        			histogram[wei] = 0
        	# print histogram
        	maximum = max(maximum, self.largestRectangleArea(histogram))
        	hei+=1
        return maximum



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

x=["10100","10111","11111","10010"]
so = Solution()
print so.maximalRectangle(x)