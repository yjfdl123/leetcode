class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==0:
        	return 0
        minp = prices[0]
        maxp = 0
        for idx,price in enumerate(prices[1:]):
        	if price-minp>maxp : maxp = price-minp
        	minp = min(minp, price)
        return maxp

so = Solution()
print so.maxProfit([3,1,5,7,4])
