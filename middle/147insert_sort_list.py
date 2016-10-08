# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lenth = 0
        node = head
        while node!=None: 
        	lenth+=1
        	node=node.next
        if lenth<2: return head
        insnode = head.next
        insprev = head
        while insnode!=None:
        	iternode = head
        	prevnode = head
        	while iternode!=insnode:
        		if insnode.val<iternode.val:
					if iternode==head:
						insprev.next = insnode.next
						insnode.next = iternode
						head = insnode
						insnode = insprev.next
					else:
						insprev.next = insnode.next
						insnode.next = iternode
						prevnode.next = insnode
						insnode = insprev.next
        		else:
        			iternode=iternode.next
        			prevnode=iternode





