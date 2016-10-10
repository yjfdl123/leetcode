#coding=utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        lst=list(str)
        while lst.count(' '): lst.remove(' ')
        if len(lst)==0: return 0
        if lst.count("+")+lst.count("-")>1: return 0
        sign=1
        while lst and not lst[0].isdigit():        	
	        if lst[0]=="-": 
	        	sign=sign*(-1)
	        	lst=lst[1:]
	        elif lst[0]=="+":
	        	lst=lst[1:]
	        else:
	        	return 0
        if len(lst)==0: return 0
        num=0
        if lst[0]=="0": return 0
        for x in lst:
        	if x.isdigit():
        		num=num*10+int(x)
        	else:
        		break
        return num*sign


"""
特殊情况：
1.有多个+-号 ,那就是0
2.有字母出现，那就计算字母以前的数字
3.空格
"""
so=Solution()
print so.myAtoi("  +1  1  1 11")
print so.myAtoi("  -0012a42")
print so.myAtoi("+-112")
print so.myAtoi("   +0 123")