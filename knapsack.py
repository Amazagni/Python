def knapsack(W,P,B): # W - waga, P - wartosc, B - max waga
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b],F[i-1][b-W[i]]+P[i])
    return F[n-1][B]
W =[10,5,13,2,156]
P =[1,2,3,4,20]
B = 15
print(knapsack(W,P,B))
