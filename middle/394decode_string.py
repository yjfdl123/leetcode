#coding=utf-8
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digits=[]
        expre = []
        idx=0
        while idx<len(s):
        	if s[idx]=="[":
        		expre.append(s[idx])
        		idx+=1
        	elif s[idx].isdigit():
        		num = 0
        		while s[idx].isdigit():
        			num = num*10+int(s[idx])
        			idx+=1
        		digits.append(num)
        	elif s[idx]=="]":
        		word = expre.pop()
        		expre.pop()
        		num = digits.pop()
        		newword = []
        		for x in range(num): newword.append(word)
        		while len(expre)>0 and expre[-1]!="[": newword.append(expre.pop())
        		newword.reverse()
        		expre.append( ''.join(newword))
        		idx+=1
        	elif s[idx].isalpha():
        		wlist = []
        		while idx<len(s) and s[idx].isalpha(): 
        			wlist.append(s[idx])
        			idx+=1
        		word = ''.join(wlist)
        		merge = [word]        	
        		while len(expre)>0 and expre[-1]!="[": merge.append(expre.pop())	
        		merge.reverse()
        		expre.append(''.join(merge))
        	# print idx-1,s[idx-1],'    ',digits,'     ',expre
        return ''.join(expre)


'''
错误：
1是右括号完合并，还是加入单词时合并,最后发现两个都是要做的
2是要注意字母前面可能会出现没有数字
'''

so=Solution()
print so.decodeString("3[ab2[de]c]")
print so.decodeString("3[a]2[bc]")
print so.decodeString("2[abc]3[cd]ef")
print so.decodeString("3[a2[c]]")










