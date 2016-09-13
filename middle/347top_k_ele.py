class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
        	if dic.has_key(num):
        		dic[num] += 1
        	else:
        		dic[num] =  1
        import heapq
        dui = []
        for key,value in dic.iteritems():
        	heapq.heappush(dui,(-value,key))
        ret = []
        for i in range(k):
        	ret.append( heapq.heappop(dui)[1] )
        return ret

x=[1,2,3,1,2,1]
so = Solution()
print so.topKFrequent(x,2)