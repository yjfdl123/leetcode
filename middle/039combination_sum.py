import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy
        candi = copy.deepcopy(candidates)
        candi.sort()
        ret = []
        self.backtracking(candi,0,target,[],ret)
        return ret

    def backtracking(self,candidates,start,target,solu,ret):
    	if target==0:
    		tmp = copy.deepcopy(solu)
    		ret.append(tmp)
    	else:
	    	for index in range(start,len(candidates)):
	    		if target -  candidates[index]>=0:
	    			solu.append( candidates[index])
	    			self.backtracking(candidates,index,target- candidates[index], solu,ret)
	    			solu.pop()
	    		else:
	    			break

x=[1,2,3,4,3,3,3]
a=x.index(3)
x.remove
print a,x

so = Solution()
print so.combinationSum([1,2,3,6,7],7)


