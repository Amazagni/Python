# sortowanie topologiczne przy pomocy DFS
# reprezentacja jako sąsiedztwo

def top(G):
    n = len(G);
    visited = [-1 for i in range(n)]
    parent = [None for i in range(n)]
    T = [None for i in range(n)]
    id = n-1
    def DFSVisit(G,u):
        nonlocal id
        visited[u] = 1
        for i in G[u]:
            if visited[i] == -1:
                parent[i] = u
                DFSVisit(G,i)
        T[id] = u
        id -= 1
    for i in range(n):
        if visited[i] == -1:
            DFSVisit(G,i)
    return T



G = [[1,2,5], #a
     [2,4], #b
     [],#c
     [],#d
     [3,6],#e
     [4],#f
     [] #g
     ]
print(top(G))
