class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="" or num2=="":
        	return ""
        lst1 = [int(s) for s in num1]
        lst2 = [int(s) for s in num2]
        lst1.reverse()
        lst2.reverse()
        if len(lst1)<len(lst2): lst1,lst2 = lst2,lst1
        lst3 = [0 for x in range(len(lst1)+len(lst2))]
        for idx2,n2 in enumerate(lst2):
        	cb = 0
        	for idx1,n1 in enumerate(lst1):
        		n3 = (n2*n1+cb) %10 
        		cb = (n2*n1+cb)/10
       			lst3[idx1+idx2] += n3
       		lst3[len(lst1)+idx2] +=cb
        lst4=[]
        cb=0
        for n3 in lst3:
        	lst4.append( (n3+cb)%10)
        	cb = (n3+cb)/10
        if cb==1: lst4.append(cb)
        while len(lst4)!=0 and lst4[-1]==0:
        	lst4.pop()
        lst4.reverse()
        lst4 = [str(n) for n in lst4]
        if lst4==[]:
        	return "0"
        else:
        	return ''.join(lst4)


x=[1,1,1,0,0,0]
while x[-1]==0:
	x.pop()
	print x

so = Solution()
print so.multiply("12345","23")
print so.multiply("11111","23")
print so.multiply("9","9")
print so.multiply("0","0")



        