# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2
        if not l2:
        	return l1
        head = None
        prev = None
        while l1 and l2:
        	newnode = None
        	if l1.val<l2.val:
        		newnode = ListNode(l1.val)
        		l1 = l1.next
        	else:
        		newnode = ListNode(l2.val)
        		l2 = l2.next
        	if not head:
        		head, prev = newnode, newnode
        	else:
        		prev.next, prev = newnode, newnode
        prev.next = l1 if l1 else l2
        return head
