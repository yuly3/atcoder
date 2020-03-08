import numpy as np


def solve():
    N, K, *A = map(int, open(0).read().split())
    A = np.array(A)
    
    X = 0
    for i in range(40, -1, -1):
        ones = np.sum((A >> i) & 1)
        zeros = N - ones
        if ones < zeros:
            if X + 2 ** i <= K:
                X += 2 ** i
        else:
            continue
    
    ans = np.sum(X ^ A)
    print(ans)


if __name__ == '__main__':
    solve()
