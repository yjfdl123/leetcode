import copy
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candi = range(10)
        ret = []
        self.backtracking(candi,1,k,n,[],ret)
        return ret
        
    def backtracking(self,candi,start,k,target,solu,ret):
    	for index in range(start,len(candi)):
    		num = candi[index]
    		if target-num>=k-1 and target-num<=(k-1)*candi[-1]:
    			if k==1:
    				if target>=1 and target<=9:
    					if solu.count(target)==0:
    						solu.append(target)
    						tmp = copy.deepcopy(solu)
    						ret.append(tmp)
    						solu.pop()
    			else:
    				solu.append(num)
    				self.backtracking(candi,index+1,k-1,target-num,solu,ret)
    				solu.pop()
so = Solution()
print so.combinationSum3(3,9)