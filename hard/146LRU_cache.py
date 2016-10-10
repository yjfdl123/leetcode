#coding=utf-8
class Node(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.head=None
        self.tail=None
        self.dic = {}

    def get(self, key):
        """
        :rtype: int
        """
        if self.dic.get(key,None):
            tmpnode = self.dic[key]
            if tmpnode!=self.head:   ##如果在头部就不用管了
                if tmpnode==self.tail: ##这是在尾部
                    self.tail = self.tail.prev
                    self.tail.next=None
                    self.head.prev=tmpnode
                    tmpnode.next=self.head
                    self.head=tmpnode
                else:                   ##这是在中间
                    tmpnode.prev.next = tmpnode.next
                    tmpnode.next.prev = tmpnode.prev
                    self.head.prev=tmpnode
                    tmpnode.next=self.head
                    self.head=tmpnode

            return self.dic[key].value
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.dic.get(key,None):          ##字典中存在，就往前移动
            tmpnode = self.dic[key]
            tmpnode.value = value
            if tmpnode!=self.head:          ##头部不用动
                if tmpnode==self.tail:      ##刚好是最后一个了
                    if tmpnode.prev: tmpnode.prev.next = None
                    self.tail = tmpnode.prev
                    self.head.prev = tmpnode
                    tmpnode.next=self.head
                    tmpnode.prev=None
                    self.head=tmpnode
                else:                       ##在中间
                    tmpnode.prev.next = tmpnode.next
                    tmpnode.next.prev = tmpnode.prev
                    self.head.prev = tmpnode
                    tmpnode.next = self.head
                    tmpnode.prev = None
                    self.head=tmpnode
        elif self.count<self.capacity:      ##字典中不存在,且容量未满
            if self.count==0:               ##第一个元素
                newnode = Node(key,value)                
                self.head=newnode
                self.tail=newnode
                self.count+=1
                self.dic[key]=newnode
                pass
            else:                           ##容量未满，非第一个元素
                newnode = Node(key,value)
                self.head.prev = newnode
                newnode.next = self.head
                self.head=newnode
                self.count+=1
                self.dic[key]=newnode
                pass
        else:                               ##字典中不存在，且容量满了
            old = self.tail.key
            self.tail = self.tail.prev
            if self.tail: self.tail.next = None
            del self.dic[old]

            newnode = Node(key,value)
            self.head.prev = newnode
            newnode.next = self.head
            self.head=newnode
            self.dic[key]=newnode
            pass
        # ttt=self.head
        # while ttt!=None:
        #     print (ttt.key,ttt.value),
        #     ttt=ttt.next
        # print self.dic, [(key,node.value) for key,node in self.dic.iteritems()]


so = LRUCache(2)
so.set(2,1)
so.set(1,1)
print so.get(2)
so.set(4,1)
print so.get(1)
print so.get(2)



"""
错误1：在删除最后一个元素时 ，两个key用了一个变量
错误2：在更新现有元素时，没有更新value
错误3：在获取元素时，没有更新位置
"""



# so = LRUCache(2)
# so.set(2,1)
# so.set(2,2)
# print so.get(2)
# so.set(1,1)
# so.set(4,1)
# print so.get(2)



# so = LRUCache(1)
# so.set(2,1)
# print so.get(2)
# so.set(3,2)
# print so.get(2)
# print so.get(3)