class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1list, v2list = version1.split('.'), version2.split('.')
        minlen = min(len(v1list), len(v2list))
    	for index in range(minlen):
    		if int(v1list[index]) > int(v2list[index]):
    			return 1
    		elif int(v1list[index]) < int(v2list[index]):
    			return -1
    	v1list.append(0)
    	v2list.append(0)
    	sum1 = reduce(lambda x,y:int(x)+int(y),v1list)
    	sum2 = reduce(lambda x,y:int(x)+int(y),v2list)
    	v1list.pop(-1)
    	v2list.pop(-1)
    	if sum1==sum2:
    		return 0
    	if len(v1list)> minlen:
    		return 1
    	elif len(v2list)>minlen:
    		return -1

print min(3,5)
v1list = "03".split('.')
sum1 = reduce(lambda x,y:int(x)+int(y),v1list)
print sum1

so=Solution()
print so.compareVersion("01","1")
print so.compareVersion("1.1","1")
print so.compareVersion("1","1.1")   #-1
