def longest_pal(T):  # T = slowo w ktorym szukamu najdluzszego palindromu
    n = len(T)
    F = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        F[i][i] = 1

    for i in range(n-1):
        if T[i] == T[i+1]:
            F[i][i+1] = 1

    for i in range(2,n):
        for j in range(n - i - 1):
            if T[j] == T[j+i] and F[j+1][j+i-1] == 1:
                F[j][j+i] = 1
    maxi = 0
    for i in range(n):
        print()
        for j in range(n):
            print(F[i][j],end = " ")
            if F[i][j] == 1:
                maxi = max(maxi, abs(i-j))
    print()
    return maxi+1
T = "qqqtaesaabaasgatww"
print(longest_pal(T))








