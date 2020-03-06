A = [5, 3, 7, 2, 1, 25, 0]
print(A)
for i in range(A.__len__()):
    for j in range(A.__len__()-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
print(A)

