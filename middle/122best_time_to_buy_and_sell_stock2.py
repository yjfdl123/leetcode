class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: return 0
        start,end = 1,len(prices)
        maxp = 0
        while start<end:
        	if prices[start]>prices[start-1]:
        		maxp+= prices[start]-prices[start-1]
        	start+=1
        return maxp
