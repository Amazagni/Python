def partition(tab,p,r):
    x = tab[r]
    i = p - 1
    for j in range(p,r):
        if tab[j] <= x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[r] = tab[r], tab[i+1]
    return i + 1 # i+1 - position of our x 

def quick_sort(tab,p,r): # r = len(tab) - 1
    if p < r:
        q = partition(tab,p,r)
        quick_sort(tab,q+1,r)
        quick_sort(tab,p,q-1)
