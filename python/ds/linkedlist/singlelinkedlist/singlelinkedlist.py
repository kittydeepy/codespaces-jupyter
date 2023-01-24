from linkedlistclass.linkedlist import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.print_list()
    linked_list.reverse_list()
    linked_list.print_list()
    linked_list.reverse_list_rec()
    linked_list.print_list()
    linked_list.prepend(100)
    print(linked_list.length_of_list())
    print(linked_list.length_of_list_rec(linked_list.head))
    '''
    linked_list.insert_after(200, "E")
    linked_list.print_list()
    linked_list.delete_node_value("C")
    linked_list.print_list()
    linked_list.delete_node_value("D")
    linked_list.print_list()
    linked_list.delete_node_pos(3)
    linked_list.print_list()
    '''

if __name__ == "__main__":
    main()