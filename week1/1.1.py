

def isort(A):
    for i in range(1, len(A)):
        j = i-1
        while (j >= 0) and (A[j] > A[j+1]):
            S1 = A[j]
            S2 = A[j+1]
            A[j] = S2
            A[j+1] = S1

            j -= 1
    


A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
isort(A)
print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
