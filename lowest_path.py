#przechodzimy po szachownicy zaczynajac lewo gora, konczac prawo dol
#kazde pole ma wartosc, szukamy najmniejszej mozliwej sciezki
def min_path(A):
    n = len(A) #A jest kwadratowa
    T =[[0 for i in range(n)] for j in range(n)]
    T[0][0] = A[0][0]
    for i in range(1,n):
        T[i][0] = T[i-1][0] + A[i][0]
        T[0][i] = T[0][i-1] + A[0][i]
    for i in range(1,n):
        for j in range(1,n):
            T[i][j] = min(T[i-1][j],T[i][j-1]) + A[i][j]
    PATH =[0 for i in range(2*n)]
    PATH[0] = A[n-1][n-1]
    x = n-1
    y = n-1
    ids = 1
    while x > 0 and y > 0:
        if T[x-1][y] < T[x][y-1]:
            PATH[ids] = A[x-1][y]
            x-=1
        else:
            PATH[ids] = A[x][y-1]
            y-=1
        ids += 1
    while x > 0:
        PATH[ids] = A[x-1][0]
        x -= 1
        ids += 1
    while y > 0:
        PATH[ids] = A[0][y-1]
        y -= 1
        ids += 1
    for i in range(1,2*n):
        print(PATH[2*n-1-i],end = " ")
    print()
    return T[n-1][n-1]
A =[[1, 1, 1, 1, 1],
    [1, 8, 9, 10, 11],
    [11, 1, 3, 4, 11],
    [9, 9, 9, 2, 1],
    [9, 9, 9, 9, 1]]
print(min_path(A))
