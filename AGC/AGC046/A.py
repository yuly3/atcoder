import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    
    ans = X * 360 // gcd(X, 360) // X
    print(ans)


if __name__ == '__main__':
    solve()
