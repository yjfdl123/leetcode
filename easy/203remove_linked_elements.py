# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev=head
        node=head
        while node!=None:
        	if node.val==val:
        		if node==head:
        			tmp=head
        			head=head.next
        			del tmp
        			node=head
        			prev=head
        		elif node.next==None:
        			prev.next=None
        			del node
        			node=None
        		else:
        			tmp=node
        			prev.next=node.next
        			node=node.next
        			del tmp
        	else:
        		prev,node=node,node.next
        return head