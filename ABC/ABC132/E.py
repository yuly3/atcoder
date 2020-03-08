def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N*3+1)]
    for i in range(M):
        u, v = map(int, input().split())
        u2, u3 = u+N, u+2*N
        v2, v3 = v+N, v+2*N
        edges[u].append(v2)
        edges[u2].append(v3)
        edges[u3].append(v)
    S, T = map(int, input().split())
    
    dist = [10**15 for _ in range(N*3+1)]
    dist[S] = 0
    que = [S]
    while que:
        que_tmp = []
        for parent in que:
            for child in edges[parent]:
                if dist[child] != 10**15:
                    continue
                que_tmp.append(child)
                dist[child] = dist[parent] + 1
        que = que_tmp
    
    if dist[T] != 10**15:
        print(dist[T]//3)
    else:
        print(-1)


if __name__ == '__main__':
    solve()