class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0 or len(triangle[0])==0:
            return 0
        ret = [0 for num in range(len(triangle[-1])) ]
        prev = [0 for num in range(len(triangle[-1])) ]

        for hei,line in enumerate(triangle):
            if hei==0:
                ret[0] = triangle[0][0]
            else:
                for wid,item in enumerate(line):
                    if wid==0: 
                        ret[wid] = item + prev[wid]
                    elif wid==len(line)-1:
                        ret[wid] = item + prev[wid-1]
                    else:
                        ret[wid] = item + min(prev[wid-1], prev[wid])
            ret, prev = prev, ret
        return min(prev)

## 这个难度就在于要使用O（n）空间处理


a=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

so = Solution()
print so.minimumTotal(a)
x=[1,2,3]
import copy
y=copy.deepcopy(x)
y.append(4)
print x,y
x,y = y,x
print x,y