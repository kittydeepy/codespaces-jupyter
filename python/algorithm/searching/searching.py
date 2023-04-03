def find_value_linear(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return True
    return False

def find_value_bt(lst, left, right, key):
    while left < right:
        mid = left + (right -left)//2

        if lst[mid] == key:
            return True
        elif key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1 
    return False

            
if __name__ == "__main__":
    lst=[3,4,5,6,7,9]
    #print(find_value_linear(lst, 13))
    print(find_value_bt(lst, 0, len(lst)-1, 5))


