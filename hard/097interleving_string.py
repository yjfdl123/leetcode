class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
       	len1,len2,len3 = len(s1),len(s2),len(s3)
       	if len1==0 and len2==0 and len3==0 : return True
       	if len1+len2!=len3: return False
       	if len1==0 : return s2==s3
       	if len2==0 : return s1==s3
       	dp = [[False for n in range(len2+1)] for m in range(len1+1)]
       	dp[0][0]=True
       	for m in range(1,len1+1):
       		dp[m][0] = dp[m-1][0] and s1[m-1]==s3[m-1]
       	for n in range(1,len2+1):
       		dp[0][n] = dp[0][n-1] and s2[n-1]==s3[n-1]
       	# print dp[0]
       	for m in range(1,len1+1):
       		for n in range(1,len2+1):
       			left =  dp[m-1][n] and (s1[m-1]==s3[m-1+n])
       			right = dp[m][n-1] and (s2[n-1]==s3[m+n-1])
       			dp[m][n] = left or right
       	return dp[len1][len2]


x=Solution()
print x.isInterleave("aabcc","dbbca","aadbbcbcac")
print x.isInterleave("aa","ab","aaba")
print x.isInterleave("aabcc","dbbca","aadbbbaccc")