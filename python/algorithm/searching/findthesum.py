# set 
# 
def findthesum_set(lst, key):
    number_dict = set()

    for element in lst:
        if key-element in number_dict:
            return [key-element, element]
        else:
            number_dict.add(element)

    return False

# Binary search
# O(nlogn) 
def findthesum_pointer(lst, key):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] + lst[right] == key:
            return (lst[left], lst[right])
        elif lst[left] + lst[right] > key:
            right -= 1
        elif lst[left] + lst[right] < key:
            left += 1
    return (0,0)

# Linear
# O(n^2) 
def findthesum_linear(lst, key):
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == key:
                return (lst[i], lst[j])
    return (0,0)

if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    #print(findthesum_pointer(lst, 10))
    #print(findthesum_linear(lst, 10))
    print(findthesum_set(lst, 10))


