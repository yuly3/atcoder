from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def solve():
    N, M = map(int, input().split())
    X = [0 for _ in range(M)]
    Y = X[:]
    for i in range(M):
        X[i], Y[i], _ = map(lambda x: int(x)-1, input().split())
    
    graph = csr_matrix(([1]*M, (X, Y)), (N, N))
    ans = connected_components(graph)[0]
    print(ans)


if __name__ == '__main__':
    solve()
