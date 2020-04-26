import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = list(input())
    N = len(S)
    
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    tmp = 0
    for i in range(N):
        si = int(S[N - 1 - i])
        tmp = (tmp + si * pow(10, i, 2019)) % 2019
        ans += d[tmp]
        d[tmp] += 1
    print(ans)


if __name__ == '__main__':
    solve()
