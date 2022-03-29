""" Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy
każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową """

def partition(tab,p,r):
    x = tab[r]
    i = p - 1
    for j in range(p,r):
        if tab[j] < x:
            i += 1
            tab[j],tab[i] = tab[i],tab[j]

    i += 1
    tab[i],tab[r] = tab[r],tab[i]
    return i

def quick_sort(tab,p,r):
    if p < r:
        q = partition(tab,p,r)
        quick_sort(tab,p,q-1)
        quick_sort(tab,q+1,r)

def zadanko(tab):
    n = len(tab)
    quick_sort(tab,0,n-1)
    flag = 0
    for i in range(n):
        first = 0
        last = n - 1
        while first <= last and tab[first] + tab[last] != tab[i]:
            if first == i: first += 1
            if last == i: last -= 1
            if tab[first] + tab[last] > tab[i]:
                last -= 1
            else:
                first += 1
        if tab[first] + tab[last] != tab[i]:
            return False
        if first == i or last == i:
            return False
    return True
