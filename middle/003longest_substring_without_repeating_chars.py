class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lsts = list(s)
        lstcom = []
        start,end = 0,len(lsts)
        maxnum=0
        while start<end:
        	# print start,lsts[start],maxnum
        	while start<end and lstcom.count(lsts[start])==0:
        		lstcom.append(lsts[start])
        		start+=1
        	if start==end: 
        		maxnum = max([len(lstcom),maxnum])
        		break
        	index = lstcom.index(lsts[start])
        	maxnum = max([len(lstcom),maxnum])
       		lstcom=lstcom[index+1:]
        return maxnum
so=Solution()
print so.lengthOfLongestSubstring("c")
x=["91","911","931","95","88","89","11"]
x.sort(reverse=True)
print x

