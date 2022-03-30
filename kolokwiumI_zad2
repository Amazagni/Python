"""2. Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie)."""
def partition(T,p,r):
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j] <= x:
            i += 1
            T[j],T[i] = T[i],T[j]
    i += 1
    T[r],T[i] = T[i],T[r]
    return i

def select(T,p,r,k):
    if p == r: return T[p]
    if p < r:
        q = partition(T,p,r)
        if k == q:
            return T[q]
        if k < q:
            return select(T,p,q-1,k)
        return select(T,q+1,r,k)

def SumBetween(T,first,last,n):
    first_num = select(T,0,len(T)-1,first)
    last_num = select(T,0,len(T)-1,last)
    summ = 0
    for i in T:
        if i >= first_num and i <= last_num:
            summ += i
    return summ

