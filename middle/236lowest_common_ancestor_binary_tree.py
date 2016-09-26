# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

    def find_lower(self,root,p,q):
    	if not root:
    		return 0, None
        depth = 1 if root==p or root ==q else 0
        depth += self.find_lower(root.left, p, q)[0] + self.find_lower(root.right, p, q)[0]

