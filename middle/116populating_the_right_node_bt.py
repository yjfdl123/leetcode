# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
    	if root!=None:
    		prev = [root]
    		while prev:
    			nex = []
    			for idx,node in enumerate(prev):
    				if idx==len(prev)-1:
    					node.next = None
    				else:
    					node.next = prev[idx+1]
    			for node in prev:
    				if node.left!=None: nex.append(node.left)
    				if node.right!=None: nex.append(node.right)
    			prev,nex = nex,[]

so = Solution()