#merge sort
def merge(tab1, tab2):
    i,j,k = 0,0,0
    l1 = len(tab1)
    l2 = len(tab2)
    tab = [0 for i in range(l1 + l2)]
    while j < l1 and k < l2:
        if tab1[j] < tab2[k]:
            tab[i] = tab1[j]
            j += 1
        else:
            tab[i] = tab2[k]
            k += 1
        i += 1
    if j == l1:
        while k < l2:
            tab[i] = tab2[k]
            i, k = i+1, k+1
    elif k == l2:
        while j < l1:
            tab[i] = tab1[j]
            i, j = i+1, j+1
    return tab

def merge_sort(tab):
    n = len(tab)
    if n == 1:
        return tab
    s = n // 2
    tab = merge(merge_sort(tab[:s]), merge_sort(tab[s:]))
    return tab

if __name__ == '__main__':
    tab = [2, 1, 15, 3, 7, 201, 19, 93]
    a = merge_sort(tab)
    for i in range(len(a)):
        print(a[i], end = " ")
