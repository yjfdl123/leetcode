class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lstm = list(magazine)
        lstr = list(ransomNote)
        dicm = {}
        for ch in lstm:
        	if dicm.get(ch,None):
        		dicm[ch]+=1
        	else:
        		dicm[ch]=1
        for ch in lstr:
        	if dicm.get(ch,None)==None:
        		return False
        	if dicm[ch]==0:
        		return False
        	dicm[ch]-=1
        return True
so = Solution()
print so.canConstruct("aa","ab")
print so.canConstruct("aa","aab")