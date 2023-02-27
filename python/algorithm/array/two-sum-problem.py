'''
This is brute force method time complecity O(n^2)
space complexity is O(1)
def two_sum_problem(A, sum)->bool:

    for i in range(len(A)-1):
        for j in range(i, len(A)):
            if A[i] + A[j] == sum:
                print(A[i], A[j])
                return True
    return False

This is brute force method time complecity O(n)
space complexity is O(n)
def two_sum_problem_ht(A, target)->bool:
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False
'''

def two_sum_problem_opt(A, target):
    i = 0
    j = len(A)-1

    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] > target:
            j -= 1
        else:
            i += 1
    return False

A = [ -2, 1, 3, 5 , 8, 10]
print(two_sum_problem_opt(A, 15))