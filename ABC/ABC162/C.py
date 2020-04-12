import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    ans = 0
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            for k in range(1, K + 1):
                tmp = gcd(i, j)
                tmp = gcd(tmp, k)
                ans += tmp
    print(ans)


if __name__ == '__main__':
    solve()
