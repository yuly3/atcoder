import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    d = defaultdict(int)
    ans = 0
    for i in range(N)[::-1]:
        ans += d[-A[i] - i]
        d[A[i] - i] += 1
    print(ans)


if __name__ == '__main__':
    solve()
