class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        time limit  时间超出限制
        """
        if len(s)==0:
        	return True
        if len(s)>len(t):
        	return False
        preline = []
        for i in range(len(s)):
        	column = []
        	if i==0:
        		for j in range(len(t)):
        			column.append(True) if (s[i]==t[j]) or ( j-1>=0 and column[j-1]) else column.append(False)
        	else:
        		for j in range(len(t)):
        			column.append(True) if ( (j-1>=0 and preline[j-1] and s[i]==t[j]) or (j-1>=0 and column[j-1])) else column.append(False)
        	preline = column
        return preline[len(t)-1]

    def isSubsequence_matrix(self, s, t):
        """
        memeory limit   存储超出限制
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
        	return True
        if len(s)>len(t):
        	return False
        matrix = []
        for i in range(len(s)):
        	column = []
        	if i==0:
        		for j in range(len(t)):
        			column.append(True) if (s[i]==t[j]) or ( j-1>=0 and column[j-1]) else column.append(False)
        	else:
        		for j in range(len(t)):
        			column.append(True) if ( (matrix[i-1][j-1] and s[i]==t[j]) or (j-1>=0 and column[j-1])) else column.append(False)
        	matrix.append(column)
        return matrix[len(s)-1][len(t)-1]






if __name__ == '__main__':
	dicts = {
		"abc":"abesce",
		"ac":"ade",
		"a":"b",
		"aebcdsd":"123aebcdsdddsd",
		"hh":"",
	}
	so = Solution()
	for key,value in dicts.iteritems():
		print key,'   ',value
		print so.isSubsequence(key, value)

	