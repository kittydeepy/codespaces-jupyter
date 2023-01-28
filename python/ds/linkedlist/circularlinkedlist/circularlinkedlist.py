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

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                curr_node = self.head
                while curr_node.next != self.head:
                    curr_node = curr_node.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    curr_node.next = self.head.next
                    self.head = self.head.next
            else:
                curr_node = self.head
                prev = curr_node
                while curr_node.next != self.head:
                    prev = curr_node
                    curr_node = curr_node.next
                    if curr_node.data == key:
                        prev.next = curr_node.next
                        #curr_node = curr_node.next
         
    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head
        print(f"Size of the list is {size}")
        
        mid = size//2
        count = 0
        curr_node = self.head

        while curr_node and count < mid:
            count += 1
            prev = curr_node
            curr_node = curr_node.next
        prev.next = self.head

        split_list = CircularLinkedList()
        while curr_node.next != self.head:
            split_list.append(curr_node.data)
            curr_node = curr_node.next
        split_list.append(curr_node.data)

        self.print_list()
        print("\n")
        split_list.print_list()




clist = CircularLinkedList()
clist.append(2)
clist.append(4)
clist.append(6)
clist.append(8)
clist.print_list()
print("-------------------")
clist.split_list()
print("-------------------")