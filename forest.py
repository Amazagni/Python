"""W lesie znajduje się n drzew stojących w jednej linii. Każde drzewo posiada określoną wartość, która
należy traktować jako zysk po jego wycięciu. Nie możemy wyciąć więcej niż dwóch drzew pod rząd.
Proszę zaimplementować funkcję pozwalającą określić które drzewa należy wyciąć, aby sumaryczny zysk
był jak największy.
"""
def forest(A):
    n = len(A)
    # zakladam ze mamy wiecej niz 3 drzewa
    f = [0] * n
    f[0] = A[0]
    f[1] = A[0]+A[1]
    f[2] = f[1] + A[2] - min(A[0],A[1],A[2])
    for i in range(3,n):
        f[i] = max(f[i-3]+A[i-1]+A[i],f[i-2]+A[i],f[i-1])
    return f[n-1]
A = [10,11,3,21,1,14,15,1,1,1,3,3]
print(forest(A))
