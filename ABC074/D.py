import numpy as np

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def solve():
    N = int(input())
    A = np.array([input().split() for _ in range(N)], dtype=np.int64).reshape(N, N)
    
    B = floyd_warshall(csr_matrix(A), directed=False)
    
    if np.any(B < A):
        print(-1)
        exit()
    
    np.fill_diagonal(B, np.inf)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if B[i][j] == np.min(B[i] + B[j]):
                A[i][j] = A[j][i] = 0
    print(np.sum(A) // 2)


if __name__ == '__main__':
    solve()
