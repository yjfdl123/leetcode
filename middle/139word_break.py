class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        lenlst = [len(word) for word in wordDict]
        minlen = min(lenlst)
        maxlen = max(lenlst)
        boolst = [False for t in s]
        for idx in range(minlen,maxlen+1):
        	if s[:idx] in wordDict:
        		boolst[idx] = True
        print boolst
        for idx in range(maxlen,len(s)):
        	for ml in range(maxlen,minlen-1,-1):
        		new = s[idx-ml+1:idx+1]
        		if new in wordDict:
        			boolst[idx] = boolst[idx] or  boolst[idx-ml]
        return boolst[len(s)-1]

x="leetcode"
y=["leet","code"]
so = Solution()
print so.wordBreak(x,y)
