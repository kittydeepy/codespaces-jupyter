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

        