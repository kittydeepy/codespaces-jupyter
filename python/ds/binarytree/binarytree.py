class Stack(object):
    def __init__(self) -> None:
        self.items = []
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def _str_(self, traversal):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Queue(object):
    def __init__(self) -> None:
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_list(self, travesal_order):
        match travesal_order:
            case "preorder":
                return self.preorder_traversal(tree.root, "")
            case "inorder":
                return self.inorder_traversal(tree.root, "")
            case "postorder":
                return self.postorder_traversal(tree.root, "")
            case "levelorder":
                return self.level_order_traversal(tree.root)
            case "reverselevelorder":
                return self.reverse_level_order_traversal(tree.root)

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
        
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def level_order_traversal(self, start):
        if start is None:
            return 
        
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
        
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_level_order_traversal(self,start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)
        stack = Stack()

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal    

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_tree(self, node):
        if node is None:
           return 0
        
        stack = Stack()
        stack.push(node)

        counter = 1
        while stack:
           node =  stack.pop()
           if node.left:
                counter += 1
                stack.push(node.left)
           if node.right:
               counter += 1
               stack.push(node.right)
        return counter 
               
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_list("preorder"))
print(tree.print_list("inorder"))
print(tree.print_list("postorder"))
print(tree.print_list("levelorder"))
print(tree.print_list("reverselevelorder"))
print(tree.height(tree.root))
print(tree.size_tree(tree.root))
