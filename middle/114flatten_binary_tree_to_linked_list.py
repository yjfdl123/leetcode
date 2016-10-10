# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        rstack=[None]
        while root:
        	if root.right!=None:
        		rstack.append(root.right)
        	if root.left!=None:
        		root.right = root.left
        		root.left=None
        	else:
        		root.right = rstack.pop()
        	root=root.right

        