# coding:utf-8
# 参考单链表结构实现一个双链表
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class Double_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        head = self.head
        while head is not None:
            current, head = head, head.next
            yield current
            # print(current.data)

    def insert_head(self, node):
        self.length += 1
        head = self.head
        if head is not None:
            self.head = node
            node.prev, node.next = None, head
            head.prev = node
        else:
            self.head, self.tail = node, node
            node.next, node.prev = None, None

    def pop_first(self):
        head = self.head
        if head is not None:
            self.head = head.next
            self.head.prev = None
            self.length -= 1
            return head
        else:
            raise Exception('pop from empty')

    def append_node(self, node):
        self.length += 1
        tail = self.tail
        if tail is not None:
            self.tail = node
            node.prev, node.next = tail, None
            tail.next = node
        else:
            self.head, self.tail = node, node
            node.next, node.prev = None, None

    def pop_end(self):
        tail = self.tail
        if tail is not None:
            self.tail = tail.prev
            self.tail.next = None
            self.length -= 1
            return tail
        else:
            raise Exception('pop from empty')

    def insert(self, index, new_node):
        if index <= 0:  # 同插入头部的方法
            self.insert_head(new_node)
        elif index >= len(self):  # 同插入尾部的方法，且能处理原链表为空的情况
            self.append_node(new_node)
        else:
            current = self.head
            while index > 1 and current.next is not None:
                current = current.next
                index -= 1
            next_node = current.next
            new_node.prev, new_node.next = current, next_node
            current.next, new_node.prev = new_node, new_node
            self.length += 1

    def remove(self, index):
        if index == 0:  # 同移除头部的方法
            self.pop_first()
        elif index == len(self) - 1:  # 同移除尾部的方法
            self.pop_end()
        elif index < 0 or index >= len(self):  # 处理超范围的情况，且能捕捉原链表为空的情况
            raise IndexError('out of index range')
        else:
            current = self.head
            while index > 1:
                current = current.next
                index -= 1
            self.length -= 1
            node = current.next
            current.next = current.next.next
            current.next.next.prev = current
            return node

    def search(self, data):
        current = self.head
        index = 0
        while current.next is not None:
            if current.data == data:
                return index
            else:
                index += 1
                current = current.next
        return -1  # 没的找到值的索引


dll = Double_LinkedList()
for i in range(5):
    node = Node(i)
    dll.insert_head(node)
print(len(dll))
print([node.data for node in dll])
dll.append_node(Node('new'))
dll.insert_head(Node('first'))
print([node.data for node in dll])
dll.pop_end()
dll.pop_first()
print([node.data for node in dll])
dll.insert(2, Node(99))
dll.remove(5)
print([node.data for node in dll])
print(dll.search(3))
