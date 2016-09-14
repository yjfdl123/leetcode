# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
        	return []
        prev, next, ret = [root], [], []
        while prev:
        	ret.append( prev[-1].val )
        	for node in prev:
	        	if node.left:
	        		next.append( node.left )
	        	if node.right:
	        		next.append( node.right)
        	prev, next = next, []
        return ret