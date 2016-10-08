# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
        	return None
        hascircle = True
        fast,slow = head,head
        while hascircle and fast!=None:
        	if fast.next!=None and fast.next.next!=None:
        		fast=fast.next.next
        		slow = slow.next
        		if fast==slow:
        			break
        	else:
        		hascircle =False
        if not hascircle:
        	return None
        else:
        	third = head
        	while third!=fast:
        		third,fast = third.next,fast.next
        return fast

