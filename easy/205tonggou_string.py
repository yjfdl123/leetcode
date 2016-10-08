class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        lst = []
        if len(s)!=len(t):
        	return False
        for idx in range(len(s)):
        	if not dic.get(s[idx],None):
        		if lst.count(t[idx])>0:
        			return False
        		dic.update({s[idx]:t[idx]})
        		lst.append(t[idx])
        	else:
        		if dic[s[idx]]!=t[idx]:
        			return False

        return True
so = Solution()
print so.isIsomorphic("aba","cdc")