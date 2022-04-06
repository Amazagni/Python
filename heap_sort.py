#heap sort
def left(i): return 2 * i + 1

def right(i): return 2 * i + 2

def parent(i): return (i - 1)//2

def heapify(tab, n, i): #Naprawianie kopca
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and tab[max_ind] < tab[l]:
        max_ind = l
    if r < n and tab[max_ind] < tab[r] :
        max_ind = r
    if max_ind != i:
        tab[max_ind],tab[i] = tab[i], tab[max_ind]
        heapify(tab, n, max_ind)

def build_heap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1): #Do 0 wlacznie wieksze niz parent(n-1) sa juz samodzielnymi kopcami
        heapify(tab, n, i)

def heap_sort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n-1, 0, -1): #Ostatni element bedzie juz posortowany
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)

if __name__ == '__main__':
    tab=[1,5,3,2,6,7,1,2,4,900,5]
    heap_sort(tab)
    for i in range(len(tab)):
        print(tab[i], end=" ")
