from stackclass.stack import Stack

def convert_dec_bin(number):
    number_stack = Stack()
    while number > 0:
        rem = number % 2
        number_stack.push(rem)
        number = number//2
    
    bin = []
    while not number_stack.is_stack_empty():
        #bin += str(number_stack.pop())
        bin = number_stack.pop()
        print(bin, end="") 


if __name__ == "__main__":
    number = int(input("Input the number: "))
    #convert_dec_bin(number)
    print(bin(number))


