class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
    	new = [str(num) for num in nums]
    	new.sort(cmp= lambda x,y:[-1,1][x+y<y+x])
    	ret=''.join(new).lstrip('0')
    	return ret if ret else "0"


x=["91","911","87","931","95","88","89"]
so=Solution()
print so.largestNumber(x)
print so.largestNumber([0,0,0])


def compare(s1,s2):
    start1,end1=0,len(s1)
    start2,end2=0,len(s2)
    while start1<end1 and start2<end2:
        if int(s1[start1])<int(s2[start2]):
            return 1
        elif int(s1[start1])>int(s2[start2]):
            return -1
        else:
            start1+=1
            start2+=1

    if end1==end2:
        return 1
    elif end1<end2:
        return -1
    else:
        return 1
# x.sort(cmp=compare)
# x.sort()
y=sorted(x,cmp=compare)
print x
print y
print [1,-1][0]