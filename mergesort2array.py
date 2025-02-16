def mergesort(A1, A2, m, n):
    A3 = [None] * (m + n)
    i = 0
    j = 0
    k = 0

    while i < m and j < n:

        if A1[i] < A2[j]:
            A3[k] = A1[i]
            k = k+1
            i = i+1
        else:
            A3[k] = A2[j]
            k=k+1
            j=j+1
    while i < m:
        A3[k] = A1[i]
        k=k+1
        i=i+1
    print("Merged Arrays: ")
    for i in range(m+n):
        print(str(A3[i]), end=" ")

A1 = [2,4,6,8]
m = len(A1)
A2 = [10,12,14,16]
n = len(A2)
mergesort(A1,A2,m,n)
