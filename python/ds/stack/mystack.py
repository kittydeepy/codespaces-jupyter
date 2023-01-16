from stackclass.stack import Stack

def main():
    mystack = Stack()
    mystack.push(100)
    mystack.push('A')
    print(mystack.print_stack())
    mystack.pop()
    print(mystack.print_stack())
    mystack.push('Z')
    print(mystack.peek())


if __name__ == "__main__":
    main()