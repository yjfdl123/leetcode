class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        start,end = 0,len(s)
        stack = []
        while start<end:
        	
