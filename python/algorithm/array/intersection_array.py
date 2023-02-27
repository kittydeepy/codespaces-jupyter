'''
A = [1,2,3,4,5]
B = [4,5,6,7,8]
print(set(A).intersection(B))
'''

def intersection_hard(A,B):
    i = 0
    j = 0
    intersection = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i = i + 1
        elif A[i] > B[j]:
            j = j + 1
        elif A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
                i = i + 1
                j = j + 1
    return intersection

A = [4,7]
B = [4,5,6,7,8]
print(intersection_hard(A,B))