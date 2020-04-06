import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S, L, R = map(int, rl().split())
    
    if S < L:
        print(L)
    elif R < S:
        print(R)
    else:
        print(S)


if __name__ == '__main__':
    solve()
