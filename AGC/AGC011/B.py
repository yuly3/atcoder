import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    A.sort()
    acc = list(accumulate(A))
    
    ans = N
    for i in range(N - 2, -1, -1):
        if 2 * acc[i] < A[i + 1]:
            ans -= i + 1
            break
    print(ans)


if __name__ == '__main__':
    solve()
