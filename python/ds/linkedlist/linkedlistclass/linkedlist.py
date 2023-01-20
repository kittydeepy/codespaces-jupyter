class Node:
    """
    Class to create node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Class to create linkedlist
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        print("\n")

    def prepend(self, data):
        curr_node = Node(data)
        curr_node.next = self.head
        self.head = curr_node

    def insert_after(self, data, data_to_be_added):
        new_node = Node(data_to_be_added)

        if self.head is None:
            return

        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                new_node.next = curr_node.next
                curr_node.next = new_node
                return
            else:
                curr_node = curr_node.next

    def delete_node_value(self, data):
        curr_node = self.head

        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None

        prev_node = None
        while curr_node:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                curr_node = None
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def delete_node_pos(self, pos):
        prev_node, curr_node = self.head
        count = 1

        if curr_node and pos == 0:
            self.head = curr_node.next
            curr_node = None
            return

        while curr_node:
            if count == pos:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                prev_node = curr_node
                curr_node = curr_node.next
                count += 1

    def length_of_list_rec(self, node):
        if node is None:
            return 0
        return 1 + self.length_of_list_rec(node.next)
     
    def length_of_list(self):
        curr_node = self.head
        count = 0

        while curr_node:
            curr_node = curr_node.next
            count += 1

        return count
    
    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        self.head = prev

    def reverse_list_rec(self):
        def _recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _recursive(curr, prev)
        self.head = _recursive(curr=self.head, prev=None)

    def merge_list(self, list2):
        p = self.head
        q = list2

        s = None

        if not p:
            return q
        elif not q:
            return p

        if p.data <= q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not q:
            s.next = p
        else:
            s.next = q
        
        return self.head = new_head

            



        