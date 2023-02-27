def array_precision_advance(A):
    A[-1] += 1

    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A



A = [9, 9, 9]
print(array_precision_advance(A))