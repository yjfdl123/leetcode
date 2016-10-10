#coding=utf-8
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path.count('/')==0:
        	return path
        pathlst = path.split('/')
        while pathlst.count('')>0: pathlst.remove('')
        stack=[]
        for char in pathlst:
        	if char==".":
        		continue
        	elif char=="..":
        		if stack:
        			stack.pop()
        	else:
        		stack.append(char)
        if len(stack)==0: 
        	return '/'
    	else:
        	return '/'+'/'.join(stack)


#有两个地方没有考虑：
#1是只有/
#2是不合格 /../..

so=Solution()
print so.simplifyPath("/../..")
print so.simplifyPath("/a/./b/../../c/")
