# Cwiczdenia 3
# MAGICZNE PIATKI!
# DOBRY PIWOT DO WYBORU
def partition(T,p,r):
    y = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def quick_sort(T,p,r):
    if p < r:
        q = partition(T,p,r)
        quick_sort(T,q+1,r)
        quick_sort(T,p,q-1)

def quick_sort_v2(T,p,r):
    while p < r:
        q = partition(T,p,r)
        quick_sort(T,q+1,r)
        r = q-1
def quick_sort_v3(T,p,r): # ograniczamy glebokosc rekurencji(max logn)
    while p < r:
        q = partition(T,p,r)
        if q - p < r - q:
            quick_sort(T,p,q - 1)
            p = q + 1
        else:
            quick_sort(T,q + 1,r)
            r = q - 1
#mniejsza polowa rekurencja
#druga iteracyjnie

#quick_sort bez rekurencji
def qsort(T):
    n = len(T)
    S = [(-1,-1) for i in range(n)] # stack
    ptr = 0 #wskazuje na koniec stosu
    S[0] = (0,n-1)
    while ptr >= 0:
        p,r = S[ptr]
        ptr -= 1
        q = partition(T,p,r)
        if p < q - 1:
            ptr += 1
            S[ptr] = p, q - 1
        if q + 1 < r:
            ptr += 1
            S[ptr] = q + 1, r

#wstawianie elementu do kopca min
class Heap:
    def __init__(self, n):
        self.T = [0 for i in range(n)]
        self.size = 0

def insert(H,e): # dodawanie do heapa elemenu e
    if len(H.T) == H.size:
        return
    H.T[H.size] = e
    H.size += 1
    i = H.size - 1
    heapify(H.T,i,0) #heapify odwrotny dziala od dolu do gory rekurentcyjnie

# Ogarnac serie naturalne
# scalanie k posortowanych list n elementowych

