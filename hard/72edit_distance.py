class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        if word1=="":
        	return len2
        if word2=="":
        	return len1
        dp = [ [0 for wid in range(len2+1)] for hei in range(len1+1)]
        for wid in range(len2+1):
        	dp[0][wid] = wid
        for hei in range(len1+1):
        	dp[hei][0] = hei
        for hei in range(1,len1+1):
        	for wid in range(1,len2+1):
        		# if word1[hei-1]==word2[wid-1]:
        		# 	dp[hei][wid] = min(dp[hei-1][wid]+1, dp[hei][wid-1]+1, dp[hei-1][wid-1])
        		# else:
        		# 	dp[hei][wid] = min(dp[hei-1][wid]+1, dp[hei][wid-1]+1, dp[hei-1][wid-1]+1)
        		dp[hei][wid] = min(dp[hei-1][wid]+1, dp[hei][wid-1]+1, dp[hei-1][wid-1]+(0 if word1[hei-1]==word2[wid-1] else 1))
        return dp[len1][len2]



so = Solution()
print so.minDistance("abcb","b")
print so.minDistance("b","abcb")
print so.minDistance("abc","abc")
print so.minDistance("ab","bcde")
print so.minDistance("a","bcde")
print so.minDistance("ab","abcde")
