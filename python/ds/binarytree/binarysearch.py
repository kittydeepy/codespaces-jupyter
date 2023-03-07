def binarysearch(data, target, low, high):

    low = 0
    high = len(data) - 1
    
    if low > high:
        return False
    else:
        mid = (low + high)// 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid + 1 

    return False