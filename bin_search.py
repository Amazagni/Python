def bin_search(tab,first,last,k):
    if first >= last:
        if first == last:
            if tab[first] == k:
                return first
        return False
    s = (first + last)//2
    if k == tab[s]:return s
    if k < tab[s]:
        return bin_search(tab,first,s-1,k)
    return bin_search(tab,s+1,last,k)
