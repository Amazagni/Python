#czy mozliwe jest utworzenie podzbiorow o sumie rownej t
def sum_tab(A,t):
    n = len(A)
    f = [[False for i in range(t+1)] for j in range(n)]
    for i in range(n):
        f[i][0] = True
    for i in range(n):
        for j in range(1,t+1):
            if j-A[i] >= 0:
                f[i][j] = f[i-1][j] or f[i-1][j-A[i]]
            else:
                f[i][j] = f[i-1][j]
    return f[n-1][t]
A=[3,5,15]
t = 19
print(sum_tab(A,t))
