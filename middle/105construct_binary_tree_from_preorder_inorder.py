# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class yanzheng(object):
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


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder :
        	return None
        if len(preorder)!=len(inorder):
        	return None
        end = len(preorder)-1
        return self.build(preorder,0,end,inorder,0,end)

    def build(self,preorder,pstart,pend,inorder,istart,iend):
    	if pend<pstart:
    		return None
    	node = TreeNode(preorder[pstart])
    	print preorder[pstart]
    	if inorder.count(preorder[pstart])==0 : 
    		return None
    	ihead = inorder.index(preorder[pstart])
    	leftnum = ihead - istart
    	rightnum = iend - ihead
    	node.left =  self.build(preorder,pstart+1,pstart+leftnum, inorder,istart,ihead-1)
    	node.right = self.build(preorder,pstart+leftnum+1,pend,   inorder,ihead+1,iend)
    	return node


x=[1,2,3,4,5,6]
y=[2,1,4,3,6,5]
so = Solution()
tree=so.buildTree(x,y)

z=yanzheng()
print z.preorderTraversal(tree)


