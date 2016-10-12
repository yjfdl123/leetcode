# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lenin = len(inorder)
        lenpo = len(postorder)
        if lenin!=lenpo:
        	return None
        else:
        	if lenin==0: return None
        	return self.loop(inorder,0,lenin-1,postorder,0,lenpo-1)

    def loop(self,inorder,instart,inend,postorder,postart,poend):
    	if instart>inend:                           ###0
    		return None
        elif instart==inend:                        ###1
            return TreeNode(inorder[instart])
        else:                                       ###>1
        	genpost = postorder[poend]
        	node = TreeNode(postorder[poend])
        	index=instart
        	while index<=inend and inorder[index]!=genpost  :
        		index+=1
        	node.left  = self.loop(inorder,instart,index-1, postorder,postart,postart+ index-instart-1)
        	node.right = self.loop(inorder,index+1,inend,   postorder,postart+index-instart,poend)
        	return node

so=Solution()
print so.buildTree([-1],[-1])
