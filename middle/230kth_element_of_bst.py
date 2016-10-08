# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.order=-1
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
        	return 0
        else:
        	self.kthSmallest(root.left,k)
        	self.order+=1
        	if self.order==k:
        		return self.root.val
        	self.kthSmallest(root.right,k)

