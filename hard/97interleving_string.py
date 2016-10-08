class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1: return s2==s3
        if not s2: return s1==s3
        if len(s1)+len(s2) != len(s3):
        	return False
        dp = [ [True for wid in range(len(s2)+1)] for hei in range(len(s1)+1)]
        for hei in range(len(s1)):
        	for wid in range(len(s2)):
        		dp[hei+1][wid+1] = (s1[hei]==s3[hei+wid] and dp[hei][wid+1]) or (s2[wid]==s3[hei+wid] and dp[hei+1][wid])
        print dp
        return dp[len(s1)][len(s2)]




so = Solution()
print so.isInterleave("aabcc","dbbca","aadbbcbcac")
# print so.isInterleave("aabcc","dbbca","aadbbbaccc")

