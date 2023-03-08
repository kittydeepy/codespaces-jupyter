'''
Complexities is O(n)
'''
def binarysearchlinear(data, target):
    for i in range(len(data) - 1):
        if data[i] == target:
            return True
    return False

'''
Complexities is O(log n)
'''
def binarysearchiterative(data, target, low, high):

    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high)// 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid + 1 

    return False

"""
complexities O(log n)
"""
def binarysearchrecursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target > data[mid] :
            binarysearchrecursive(data, target, mid + 1, high)
        else:
            binarysearchrecursive(data, target, low, mid-1)
