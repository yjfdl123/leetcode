# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None: return True
        prev,nex = [root],[]
        while prev:
        	if len(prev)==prev.count(None): break
        	for node in prev:
        		if node!=None: 
        			nex.append(node.left)
        		else:
        			nex.append(None)
        		if node!=None:
        			nex.append(node.right)
        		else:
        			nex.append(None)
        	start,end = 0, len(nex)-1
        	while start<end:
        		if nex[start]==None and nex[end]!=None:
        			return False
        		if nex[start]!=None and nex[end]==None:
        			return False
        		if nex[start]!=None and nex[end]!=None and  nex[start].val!=nex[end].val: 
        			return False
        		start+=1
        		end-=1
        	prev,nex = nex,[]
        return True

x=[1,2,3,None,None]
print x.count(None)
