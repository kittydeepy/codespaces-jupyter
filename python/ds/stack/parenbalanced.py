from stackclass.stack import Stack

def is_match(str_char, stk_char):
    if stk_char == "{" and str_char == "}":
        return True
    elif stk_char == "[" and str_char == "]":
        return True
    elif stk_char == "(" and str_char == ")":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    string_stack = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        if paren_string[index] in "[{(":
            string_stack.push(paren_string[index])
        else:
            if string_stack.is_stack_empty():
                return False
                break
            else:
                top = string_stack.pop()
                if is_match(paren_string[index], top):
                    is_balanced = True
                else:
                    is_balanced = False
                    break
        index += 1
    
    if string_stack.is_stack_empty() and is_balanced:
        return is_balanced
    else:
        return False

        
if __name__ == "__main__":
    string = input("Enter the parenthessis to be tested: ")
    print(is_paren_balanced(string))