#coding=utf-8
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="": return 0
        ret=0
        start,end=0,len(s)
        stack=[1]                      #存储当前处理括号的符号
        cur=1
        while start<end:
            if s[start].isdigit():       #数字处理,取出stack[-1]进行叠加
                num=0
                while s[start].isdigit():
                    num=num*10+int(s[start])
                    start+=1
                ret = ret + cur*num
            elif s[start]==")":          #pop
                stack.pop()
                start+=1
            elif s[start]==" " :          #是空格忽略
                start+=1
            elif s[start]=="(":           ##开始变号
                stack.append(stack[-1]*cur)
                cur=1
                start+=1
            else:                    #+-要变号
                cur=stack[-1] if s[start]=="+" else -stack[-1]
                start+=1
        return ret




so = Solution()
print so.calculate("100 + 100 3")
print so.calculate("(1+(4+5+2232)- 3)+(6+ 8)")
