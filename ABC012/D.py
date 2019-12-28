from scipy.sparse import csr_matrix
from scipy.sparse.csgraph._shortest_path import floyd_warshall


def solve():
    N, M = map(int, input().split())
    dist = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        dist[a-1][b-1] = t
        dist[b-1][a-1] = t
    fw = floyd_warshall(csr_matrix(dist))
    
    ans = 300*1000
    for i in range(N):
        dist_max = 0
        for j in range(N):
            if i == j:
                continue
            dist_max = max(dist_max, fw[i][j])
        ans = min(ans, dist_max)
    print(int(ans))


if __name__ == '__main__':
    solve()
