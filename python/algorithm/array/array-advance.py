def array_advance(A)->bool:
    further_reached = 0
    last_index = len(A) - 1
    i = 0

    while i <= further_reached and further_reached < last_index:
        further_reached = max(further_reached, A[i]+i)
        #print(i, further_reached)
        print(f"{i} <= {further_reached} and {further_reached} < {last_index}")
        i = i + 1
    
    return further_reached >= last_index

A = [ 1,2,3,4]
print(array_advance(A))
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))

