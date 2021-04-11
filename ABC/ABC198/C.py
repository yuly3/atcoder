import sys
from math import hypot, ceil

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    R, X, Y = map(int, rl().split())
    
    dist = hypot(X, Y)
    if dist < R:
        print(2)
        exit()
    print(int(ceil(dist / R)))


if __name__ == '__main__':
    solve()
