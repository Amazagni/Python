class PQ:
    def __init__(self,n):
        self.tab = [None] * n
        self.size = 0


    def heapify(self,n,i):#n - size,
        l = 2 * i + 1
        r = 2 * i + 2
        maxx = i
        if l < n and self.tab[l] > self.tab[maxx]:
            maxx = l
        if r < n and self.tab[r] > self.tab[maxx]:
            maxx = r
        if maxx != i:
            self.tab[i],self.tab[maxx] = self.tab[maxx],self.tab[i]
            self.heapify(n,maxx)


    def add(self,k):
        self.tab[self.size] = k
        self.tab[self.size],self.tab[0] = self.tab[0],self.tab[self.size]
        for i in range((self.size-1)//2,-1,-1):
            self.heapify(self.size + 1,i)
        self.size += 1
