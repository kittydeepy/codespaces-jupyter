class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def prepend(self,data):
        new_node = Node(data)
        curr_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node

        self.head = new_node


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next =  self.head
        else:
            new_node = Node(data)
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break


clist = CircularLinkedList()
clist.append(2)
clist.append(4)
clist.append(6)
clist.print_list()
clist.prepend(1)
clist.print_list()