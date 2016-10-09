#coding=utf-8
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lens,lent = len(s),len(t)
        if lens<lent : return 0
        dp = [[0]*(lent+1) ]*(lens+1)
        dp[0][0]=1
        for m in range(1,lens+1):
        	for n in range(1,lent+1):
        		if dp[m-1][n]>0:   #m-1已经包含了前n个元素
        			if s[m-1]==t[n-1]:
        				dp[m][n]=dp[m-1][n]+1
        			else:
        				dp[m][n]=dp[m-1][n]
        		elif dp[m-1][n-1]>0 and s[m-1]==t[n-1]:
        			dp[m][n]=dp[m-1][n-1]
        	print dp[m]
        return dp[lens][lent]
so = Solution()
# print so.numDistinct("rabbbit","rabbit")
# print so.numDistinct("abcde","ace")
print so.numDistinct("eee","eee")


