#encoding=utf-8
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
        	return 0
        stack = []
        idx = 0
        maxarea = 0
        while idx<len(heights):
        	if not stack:
        		stack.append(idx)
        	else:
        		l_idx = stack[-1]
    			while stack and heights[ stack[-1]] > heights[idx]:
    				s_idx = stack.pop()
    				maxarea = max(maxarea, heights[s_idx]*(l_idx-s_idx+1))
    			stack.append(idx)
        	idx+=1
        for idx in stack:
        	maxarea = max(maxarea, (stack[-1]-idx+1)*heights[idx] )
        return maxarea

## 这个解法的关键之处：原来我一直没有搞清楚，是要计算最小到最大的，还是实践出真知

so = Solution()
a=[2,1,5,6,2,3]
print so.largestRectangleArea(a)
print so.largestRectangleArea([1,0,1,1,0,0])
