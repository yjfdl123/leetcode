# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tran = []
        if root:
        	tran.append(root.val)
        	tran.extend( self.preorderTraversal( root.left) )
        	tran.extend( self.preorderTraversal( root.right) )
        return tran

from heapq import *
import heapq
print help(heapq)
x=[3,2,4,5,6,2]
print nlargest(3,x)
print nsmallest(3,x)


