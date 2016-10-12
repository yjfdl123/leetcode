# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxpath,maxsum = self.find(root)
        return maxsum
    def find(self,root):
    	if root==None:
    		return 0,-sys.maxint-1
    	if root.left==None and root.right==None:
    		return root.val,root.val
    	leftmaxpath, leftmaxsum =self.find(root.left)
    	rightmaxpath,rightmaxsum=self.find(root.right)
    	if leftmaxpath<0: leftmaxpath=0
    	if rightmaxpath<0: rightmaxpath=0
    	maxpath = max([leftmaxpath,rightmaxpath])+root.val
    	maxsum = max([leftmaxpath+rightmaxpath+root.val,leftmaxsum,rightmaxsum])
    	return maxpath,maxsum