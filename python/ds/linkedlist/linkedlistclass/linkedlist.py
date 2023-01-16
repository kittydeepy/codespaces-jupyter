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

    def append(self, data)