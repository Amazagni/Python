# Sortowanie lancucha przez wybieranie
# Szukamy największego, tworzymy nowa liste i lecimy od najwiekszej (latwiejsze dodawanie kolejnych elementów)
# Z wartownikiem (na początku)
# Zlozonosc N(N+1)/2 (ciag arytmetyczny n + n-1 + ... + 1)
class Node():
    def __init__(self,key):
        self.data=key
        self.next=None
def findmax(first):
    maxel = first.next
    maxprev = first
    tmp = first.next
    prevtmp = first
    while(tmp != None):
        if(maxel.data < tmp.data):
            maxprev = prevtmp
            maxel = tmp
        prevtmp = tmp
        tmp = tmp.next
        maxprev.next = maxel.next
        return maxel

def sort(first):
    res = None
    guard = Node(-1)
    guard.next = first
    first = guard
    while(first.next != None):
        maxx = findmax(first)
        maxx.next = res
        res = maxx
    return res


