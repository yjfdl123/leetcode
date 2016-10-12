class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s=="":return True
        lenlst = [len(word) for word in wordDict]
        if lenlst==[]:return False
        minlen = min(lenlst)
        maxlen = max(lenlst)
        ret=[0]*(len(s)+1)
        ret[0]=1
        # print ret
        for idx in range(1,len(s)+1):
            for word in wordDict:
                start= idx-len(word)+1

                if start>=1:
                    # print "start:",start,s[start:]
                    # print idx,start,word,ret[start-1],s[start-1:idx],s
                    if ret[start-1]==1 and s[start-1:idx]==word:
                        ret[idx]=1
                        break
            # print idx,ret
        return True if ret[len(s)]==1 else False




x="bb"
y=["a","b","bbb","bbbb"]
so = Solution()
print so.wordBreak(x,y)
