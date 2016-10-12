class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic={char:0 for char in t}
        count=0
        slow,fast=0,0
        lens,lent=len(s),len(t)
        minimum=lens
        ret=""
        while slow<=fast and fast<lens:
        	if count<lent:
        		if dic.get(s[fast],None)!=None:
        			if dic[s[fast]]==0:
        				count+=1
        			dic[s[fast]]+=1     
        		# if fast<lens-1: 
        		fast+=1   		
        	elif count==lent:
        		# print 'begin:',slow,fast,dic
        		while count==lent:
        			if dic.get(s[slow],None):
        				dic[s[slow]]-=1
        				if dic[s[slow]]==0:
        					count-=1
        			slow+=1
        		if minimum>=fast-slow+2:
        			minimum=fast-slow+2
        			ret=s[slow-1:fast]
        		# print 'end:',slow,fast,dic
        	# print dic
        if count==lent:
    		while count==lent:
    			if dic.get(s[slow],None):
    				dic[s[slow]]-=1
    				if dic[s[slow]]==0:
    					count-=1
    			slow+=1
    		if minimum>=fast-slow+2:
    			minimum=fast-slow+2
    			ret=s[slow-1:fast]
        return ret

# S = "ADOBECODEBANC"
# T = "ABC"
S="A"
T="A"
so=Solution()
print so.minWindow(S,T)