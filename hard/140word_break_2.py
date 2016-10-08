class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        import copy
        if s=="" or wordDict==[]:
        	return []
        if not wordDict:
        	return []
        lst = [len(word) for word in wordDict]
        minl = min(lst)
        maxl = max(lst)
        ret = {idx:[] for idx in range(len(s)+1)}
        for idx in range(minl,len(s)+1):
        	# for mr in range(minl,maxl+1):
        	for mr in range(maxl,minl-1,-1):
        		if idx>=mr :
        			new = s[idx-mr:idx]
        			# if wordDict.count(new)>0:
        			if new in wordDict:
        				lastend = idx-mr
        				tmp = copy.deepcopy(ret[lastend])
        				if tmp==[]:
        					tmp = [[new]]
        				else:
        					[key.append(new) for key in tmp]
        				ret[idx].extend(tmp)
       	sen =[]
        for line in ret[len(s)]:
        	sen.append(' '.join(line))
        return sen






s="catsanddog"
dic= ["cat", "cats", "and", "sand", "dog"]
so=Solution()
print so.wordBreak(s,set(dic))