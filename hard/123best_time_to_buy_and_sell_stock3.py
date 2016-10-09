class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length<2: return 0
        pre,post= [0]*length, [0]*length
        minimum = prices[0]
        start=1
        while start<length:
        	# if prices[start]>minimum:
        		# pre[start] = prices[start]-minimum
        	pre[start] = max(prices[start]-minimum, pre[start-1])
        	minimum = min(minimum,prices[start])
        	start+=1
        print pre
        end=length-2
        maximum=prices[-1]
        while end>=0:
        	# if prices[end]<maximum:
        	# 	post[end] = maximum- prices[end]
        	post[end] = max( maximum- prices[end], post[end+1])
        	maximum = max(maximum, prices[end])
        	end-=1
        maxp = 0
        start=0
        while start<length:
        	maxp = max(maxp, pre[start]+post[start])
        	start+=1
        return maxp

so = Solution()
print so.maxProfit([3,10,4,7])

