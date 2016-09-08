class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isfushu = True if x<0 else False
        x=-x if isfushu else x
        num=[]
        while x>0:
        	num.append(x%10)
        	x=x/10
        ret=0
        for item in num:
        	ret = ret*10 + item
        ret = -ret if isfushu else ret
        if ret>2147483647:
            return 0
        if ret<-2147483647:
        	return 0
        


        return ret


'''
	容易出错的地方：计算出的数值要不超出int范围
'''



if __name__=="__main__":
	xx = [123,321,-123,0,1534236469]
	so = Solution()
	y=[so.reverse(item) for item in xx]
	print y