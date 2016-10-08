class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """        
        pat = list(pattern)
        st = str.split(' ')
        st = [value for value in st if value!=""]
        if len(pat)!=len(st):
        	return False
        dic = {}
        lis = []
        for idx,item in enumerate(pat):
        	if not dic.get(item,None):
        		if lis.count(st[idx])>0:
        			return False
        		dic.update( {item:st[idx]} )
        		lis.append(st[idx])
        	else:
        		if dic[item]!=st[idx] : return False
        return True


so = Solution()
print so.wordPattern("abba","dog cat cat     dog")
print so.wordPattern("abba","dog cat cat fish")
print so.wordPattern("abba","dog dog dog")