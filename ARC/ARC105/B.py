import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    a = list(map(int, rl().split()))
    
    num = a[0]
    for ai in a[1:]:
        num = gcd(num, ai)
    print(num)


if __name__ == '__main__':
    solve()
