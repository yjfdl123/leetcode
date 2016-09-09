#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
        	delnode = node.next
        	node.val = delnode.val
        	node.next = delnode.next
        	del delnode

    def createlist(self,nums):
    	if len(nums)==0:
    		return None
    	head = ListNode(nums[0])
    	prev, nextnode = None, None
    	for index in range( len(nums) ):
    		if index==0:
    			prev = head
    		else:
    			nextnode = ListNode(nums[index])
    			prev.next = nextnode
    			prev = nextnode
    	return head

    def printlist(self,head):
    	node = head
    	while node:
    		print node.val,'-->',
    		node = node.next
    	print 



if __name__ == '__main__':
	so = Solution()
	lists=[ [1,3,5,7],[3],[1],[],[2,4,3,8]]
	for lst in lists:
		head = so.createlist(lst)
		so.printlist(head)
		so.deleteNode(head)
		so.printlist(head)


