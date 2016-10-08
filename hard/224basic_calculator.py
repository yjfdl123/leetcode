import re
class Solution(object):
    def cal_plus(self,stack):
    	print stack
    	idx=0
        ret=stack[idx]
        idx+=1
        while idx<len(stack):
            fuhao = stack[idx]
            num = stack[idx+1]
            idx+=2
            if fuhao=="+":
                ret+=num
            elif fuhao=="-":
                ret-=num
        return ret
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        start, end = 0,len(s)
        left = ["("]
        cal = ["+","-"]
        right = [")"]
        pat = re.compile("^\d+")

        while start<end:
            digit = pat.findall(s[start:])
            if digit:
                stack.append(int(digit[0]))
                start+=len(digit[0])
                continue
            if left.count(s[start])>0 or cal.count(s[start])>0:
                stack.append(s[start])
                start+=1
            elif right.count(s[start])>0:
                idx=len(stack)-1
                while stack[idx]!=left[0]:
                    idx-=1
                idx+=1
                ret = self.cal_plus(stack[idx:])
                while stack[-1]!=left[0]: stack.pop()
                stack.pop()
                stack.append(ret)
                start+=1
            elif s[start]==' ':
                start+=1
        if stack:
        	return self.cal_plus(stack)


pat=re.compile("^\d+")
x="d123csd32dfsdvd"
y=pat.findall(x)
print y

print "3".isdigit()

so = Solution()
print so.calculate("100 + 100 3")
print so.calculate("(1+(4+5+2232)- 3)+(6+ 8)")
z=Basic Calculator
