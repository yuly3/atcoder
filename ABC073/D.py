from itertools import permutations

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph._shortest_path import floyd_warshall


def solve():
    N, M, R = map(int, input().split())
    r = list(map(lambda x: int(x)-1, input().split()))
    dist = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        dist[A-1][B-1] = C
        dist[B-1][A-1] = C
    fw = floyd_warshall(csr_matrix(dist))
    
    
    ans = 10**12
    for visit in permutations(r, R):
        m_sum = 0
        for i in range(R-1):
            m_sum += fw[visit[i]][visit[i+1]]
        ans = min(ans, m_sum)
    print(int(ans))


if __name__ == '__main__':
    solve()
