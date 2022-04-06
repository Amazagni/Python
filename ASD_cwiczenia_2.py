#scalanie iteracyjne link list
def merge_iterative(p1,p2):
    new = Node()
    res = new
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            new.next = p1
        else:
            new.next = p2
        new = new.next
    if p1 is None:
        new.next = p2
    else:
        new.next = p1
    return res.next


#scalanie list czesciowo posortowanych
# 1 3 5 | 2 6 | 3 6 9 | 1 2 3 | 0 1
# 1 2 3 5 6 | 1 2 3 3 6 9 | 0 1 # wazne zeby robic wiele mergow w jednym czasie (mniejsza zlozonosc)
# ciagle szukamy nowych posortowanych ciagow i je scalamy
def cut_series(head):
    while head.next is not None and head.val <= head.next.val:
        head = head.next
    res = head.next
    head.next = None
    return res

def merge_sort(head):
    if head is None:
        return head, False
    new = cut_series(head)
    if new is None:
        return head, False
    newer = cut_series(new)
    merged = merge(head, new)
    if newer is None:
        return head, True
    else:
        tail.next = newer
        merge_sort(newer)
        return merged, True  #TUTAJ BRAKUJE WIELE ALE NO CUSZ OGOLNIE DA SIE OGARNAC ZAMYSL
def merge_out(head):
    while True:
        h,f = merge_sort(head)
        if f == False:
            return h
        else:
            head = h


# posortowana tablica
# A[i] + A[j] = S bin search'em gdzie p = i zlozonosc nlogn
# zaczynamy i = 0 ; j = n   gdy i + j > S j--  gdy i + j < S i++ gdy i j sie zamienia sie miejscami nie ma takiego w tablicy




# Lider ciagu - liczba wystepujaca czescien niz n//2
# wykreslamy po dwie rozne od siebie cyferki
