class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst1,lst2 = list(s),list(t)
        len1,len2=len(s),len(t)
        if len1!=len2: return False
        dic1 = {}
        for ch in lst1:
        	if dic1.get(ch,None):
        		dic1[ch]+=1
        	else:
        		dic1.update({ch:1})
        for ch in lst2:
        	if dic1.get(ch,None) or dic1.get(ch)<1:
        		return False
        	else:
        		dic1[ch]-=1
        return True
so =Solution()
print so.isAnagram("a","b")
print so.isAnagram("a","a")
