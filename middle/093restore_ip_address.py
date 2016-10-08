import copy
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        if len(s)>12 or len(s)<4: return ret
        self.find_new(s,4,len(s)-1,[],ret)
        res=[]
        for key in ret:
        	key.reverse()
        	res.append('.'.join(key))
        return res
        

    def find_new(self,s,order,end,cur,ret):
    	if order==1 :
    		if int(s[:end+1])==0 and end>0: 
    			return
    		if end>0 and s[0]=='0':
    			return 
    		ip = s[:end+1]
    		if int(ip)<=255 and int(ip)>=0 :
	    		cur.append(s[:end+1])
	    		x=copy.deepcopy(cur)
	    		ret.append(x)
	    		cur.pop()
    	else:
	    	for idx in range(3):
	    		start=end-idx	    		
	    		if start<=3*(order-1) and start>=0:
	    			ip = s[start:end+1]	    			
	    			if ip=="0" or ip[0]!='0' :
	    				if int(ip)<=255 and int(ip)>=0 :
	    					print ip,int(ip)
		    				cur.append(ip)
		    				# print "order:",order,"idx:",idx,"ip:",ip,"start:",start,"end:",end,"cur:",cur
		    				if start+1>=order:
		    					self.find_new(s,order-1,start-1,cur,ret)
		    				cur.pop()
		    				# print "------------order:",order,"idx:",idx,"ip:",ip,"start:",start,"end:",end,"cur:",cur

so = Solution()
# print so.restoreIpAddresses("25525511135")
# print so.restoreIpAddresses("111000")
# print so.restoreIpAddresses("010010")/
# print so.restoreIpAddresses("10101010")
print so.restoreIpAddresses("9999999")

