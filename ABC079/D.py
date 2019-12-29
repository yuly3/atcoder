from scipy.sparse import csr_matrix
from scipy.sparse.csgraph._shortest_path import floyd_warshall


def solve():
    H, W = map(int, input().split())
    c = [[] for _ in range(10)]
    for i in range(10):
        c[i] = list(map(int, input().split()))
    A = [[] for _ in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))
    
    fw = floyd_warshall(csr_matrix(c))
    power = [0 for _ in range(10)]
    for i in range(10):
        if i == 1:
            continue
        power[i] = fw[i][1]
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == -1 or A[i][j] == 1:
                continue
            ans += power[A[i][j]]
    print(int(ans))


if __name__ == '__main__':
    solve()
