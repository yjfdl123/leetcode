# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
        	return None
        tail=head
        while tail.next!=None:
        	tail=tail.next
        return self.buildtree(head,tail)

    def buildtree(self,head,tail):
    	if head==tail:
    		treenode = TreeNode(head.val)
    		return treenode
    	slow,fast=head,head
    	prev=head
    	while fast!=tail:
    		prev=slow
    		slow=slow.next
    		fast=fast.next
    		if fast!=tail:
    			fast=fast.next
    	treenode=TreeNode(slow.val)
    	treenode.left = self.buildtree(head,prev)
    	if slow!=fast:
    		treenode.right = self.buildtree(slow.next,tail)
    	return treenode


