class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            #new_node.next = None
    
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def add_node_after(self, data_to_add, after_this_data):
        if self.head is None:
            new_node = Node(data_to_add)
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.next is None and curr_node.data == after_this_data:
                    self.append(data_to_add)
                    return
                else:
                    new_node = Node(data_to_add)
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                    new_node.prev = curr_node
                    curr_node.next.prev = new_node
                    return
                curr_node = curr_node.next

    def reverse(self):
        curr_node = self.head
        tmp = None
        while curr_node:
            tmp = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = tmp
            curr_node = curr_node.prev
            if tmp:
                self.head = tmp.prev

    def delete_node(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key and curr_node == self.head:
                #case - 1 
                if not curr_node.next:
                    curr_node = None
                    self.head = None
                    return
                else:
                #case - 2
                    curr_node.next.prev = None
                    curr_node.next = None
                    curr_node = None
                    self.head = curr_node.next
                    return
            elif curr_node.data == key:
                if curr_node.next:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    curr_node.next = None
                    curr_node.prev = None
                    curr_node = None
                    return
                else:
                    curr_node.prev.next = None
                    curr_node.prev = None
                    curr_node.next = None
                    curr_node = None

            curr_node = curr_node.next
    
    def remove_duplicate(self,data):
        curr_node = self.head
        seen = dict()
        while curr_node:
            if curr_node.data not in seen:
                seen[curr_node.data] = 1
                curr_node = curr_node.next
            else:
                self.remove_duplicate(curr_node.data)
                curr_node = curr_node.next
    
    def pair_sum(self, sum):
        pair1 = self.head
        pair2 = None
        combination_list = list()

        while pair1:
            pair2 = pair1.next
            while pair2:
                if pair1.data + pair2.data == sum:
                    combination_list.append("(" + str(pair1.data) +"," + str(pair2.data) +")")
                pair2 = pair2.next
            pair1 = pair1.next
        return combination_list

    
    def add_node_before(self, key , data):
        curr_node = self.head
        while curr_node:
            if curr_node.prev is None and curr_node.data == key:
                self.prepend(data)
                return
            else:
                new_node = Node(data)
                curr_node.prev.next = new_node
                curr_node.prev = new_node
                new_node.prev = curr_node.prev
                new_node.next = curr_node
                return
            curr_node = curr_node.next

                




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

dllist = DoubleLinkedList()
dllist.append(20)
dllist.append(30)
dllist.print_list()
dllist.prepend(10)
dllist.print_list()