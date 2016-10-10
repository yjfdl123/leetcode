class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10: return []
        dic={}
        for idx in range(len(s)-10+1):
        	seq = s[idx:idx+10]
        	if dic.get(seq,None):
        		dic[seq]+=1
        	else:
        		dic[seq]=1
        ret= [key for key,value in dic.iteritems() if value>1 ]
        return ret
so=Solution()
print so.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")