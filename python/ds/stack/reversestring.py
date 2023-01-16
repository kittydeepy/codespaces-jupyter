from stackclass.stack import Stack

def main():
    stack = Stack()
    string = "testing"
    print(string)
    for c in string:
        stack.push(c)
    rev_string = []
    while not stack.is_stack_empty():
        rev_string.append(stack.peek())
        stack.pop()
    for c in rev_string:
        print(c,end="")
    #print(rev_string,sep="")

if __name__ == "__main__":
    main()