# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):    
    @staticmethod
    def create_tree(nums):
        if not nums :
            return None
        length = len(nums)

        nodelist = []
        for num in nums:
            nodelist.append( TreeNode(num) )
        for index in range(len(nums)):
            if nodelist[index]:
                nodelist[index].left = nodelist[2*index + 1] if 2*index+1<length else None
                nodelist[index].right = nodelist[2*index + 2] if 2*index+2<length else None
        head = nodelist[0]
        del nodelist
        return head

    @staticmethod
    def print_tree(head):
        if not head:
            print None
            return

        nodelist = [head,0]
        while nodelist:
            node = nodelist.pop(0)
            if isinstance(node,int):
                if nodelist:
                    nodelist.append(node+1)
                    print 
                else:
                    print "\n"
                    return
            else:
                if node:
                    print node.val,
                    if node.left:
                        nodelist.append(node.left)
                    if node.right:
                        nodelist.append(node.right)

    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return 0
        return 0 if not root else max( self.maxDepth(root.left)+1, self.maxDepth(root.right)+1 )

if __name__ == '__main__':
    trees=[ 
            [0,1,2,3,4,5,6,7,8,9],
            [123,2345],
            [0,1,2,3,4],
            [1],
            [1,None,2,None,None,3],
    ]
    for  tree in trees:
        print tree
        head = BinaryTree.create_tree(tree)
        BinaryTree.print_tree(head)
        print "depth:",BinaryTree().maxDepth(head)