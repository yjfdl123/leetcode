# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
        	return True
        if (p and not q) or (q and not p):
        	return False
        return False if p.val!=q.val else self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)



'''
	要先判断是否为None，才能使用val