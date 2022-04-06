#RADIX SORT
#chr(120) = 'A', ord('A') = 120
def selection_sort(tab,j,n):
    select = [[] for i in range(251)]
    for i in range(n):
        select[ord(tab[i][j])].append(tab[i])
    indeks = 0
    for i in range(251):
        for indekss in range(len(select[i])):
            tab[indeks] = select[i][indekss]
            indeks += 1

def radix_sort(tab,k,n):# k - dlugosc liter
    for i in range(k-1, -1, -1):
        selection_sort(tab,i,n)
