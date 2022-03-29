"""Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową."""

#zlozonosc logn + (p-q)log(p-q)

def partition(tab,p,r):
    x = tab[r]
    i = p - 1
    for j in range(p,r):
        if tab[j] <= x:
            i += 1
            tab[j],tab[i] = tab[i],tab[j]
    i += 1
    tab[r],tab[i] = tab[i],tab[r]
    return i

def quick_sort(tab,p,r):
    if p < r:
        q = partition(tab,p,r)
        quick_sort(tab,p,q-1)
        quick_sort(tab,q+1,r)

def select(tab,p,k,r):
    if p==r: return tab[p]
    if p < r:
        q = partition(tab,p,r)
        if k == q: return tab[q]
        elif k < q: return select(tab,p,k,q-1)
        else: return select(tab,q+1,k,r)

def section(tab,first,last):
    n = len(tab)
    first_number = select(tab,0,first,n-1)
    last_number = select(tab,0,last,n-1)
    neww = []
    for i in tab:
        if i >= first_number and i <= last_number:
            neww.append(i)
    quick_sort(neww,0,len(neww)-1)
    return neww
tab = [1,2,65,1.2,3.6,4.6,7,3]

print(section(tab,3,7))
