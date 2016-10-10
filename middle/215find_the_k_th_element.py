class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        queue = []
        for num in nums:
        	if len(queue)<k:
        		heapq.heappush(queue,num)
        	else:
        		heapq.heappush()