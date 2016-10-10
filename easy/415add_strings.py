class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="": return num2
        if num2=="": return num1
        lst1 = [int(x) for x in num1]
        lst2 = [int(x) for x in num2]
        if len(lst1)<len(lst2): lst1,lst2=lst2,lst1
        lst1.reverse()
        lst2.reverse()
        while len(lst2)!=len(lst1): lst2.append(0)
        carry=0
        for index in range(len(lst1)):
        	tmp =  lst1[index]+lst2[index]+carry	
        	lst1[index] = (tmp)%10
        	carry = tmp/10
        if carry==1: lst1.append(1)
        lst1.reverse()
        ret=[str(x) for x in lst1]
        return ''.join(ret)
so=Solution()
print so.addStrings("1234","0000")
