def findclosenumber(A, target):
    min_diff = min_diff_left = min_diff_right = float('inf')
    low = 0
    high = len(A) - 1
    closet_number = 0

    if len(A) == 0:
        return None
    if len(A) == 1:
        return 1
    
    while low < high:
        mid = (low + high) // 2
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1]- target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] + target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closet_number = A[mid-1]
        if min_diff_right > min_diff:
            min_diff = min_diff_right
            closet_number = A[mid+1]
        
        if target > A[mid]:
            low = mid + 1
        elif target < A[mid]:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
        
    return closet_number