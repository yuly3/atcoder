from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def solve():
    N, M, L = map(int, input().split())
    dist = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        dist[a-1][b-1] = c
        dist[b-1][a-1] = c
    fw = floyd_warshall(csr_matrix(dist))

    ok = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if fw[i][j] <= L:
                ok[i][j] = 1
    ans = floyd_warshall(csr_matrix(ok))

    Q = int(input())
    for i in range(Q):
        s, t = map(lambda x: int(x)-1, input().split())
        if ans[s][t] < N:
            print(int(ans[s][t])-1)
        else:
            print(-1)


if __name__ == '__main__':
    solve()