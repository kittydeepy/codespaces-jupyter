from linkedlistclass.linkedlist import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append(100)
    linked_list.prepend("D")
    linked_list.insert_after("B", "C")
    linked_list.print_list()
    linked_list.delete_node_value("C")
    linked_list.print_list()
    linked_list.delete_node_value("D")
    linked_list.print_list()
    linked_list.delete_node_pos(3)
    linked_list.print_list()

if __name__ == "__main__":
    main()