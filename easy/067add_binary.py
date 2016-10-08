class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="" : return b
        if b=="" : return a
        lst1 = [int(x) for x in a]
        lst2 = [int(x) for x in b]
        lst1.reverse()
        lst2.reverse()
        if len(lst1)<len(lst2): lst1,lst2=lst2,lst1
        while len(lst2)!=len(lst1): lst2.append(0)
        carry = 0
        for idx in range(len(lst1)):
        	ss = lst1[idx]+lst2[idx]+carry
        	lst1[idx] = ss%2
        	carry = ss/2
        if carry==1: lst1.append(1)
        lst1.reverse()
        ret = [str(x) for x in lst1]
        return ''.join(ret)

so = Solution()
print so.addBinary("111","1")