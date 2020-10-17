import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    T = rl().rstrip()
    
    if S == 'Y':
        print(T.upper())
    else:
        print(T)


if __name__ == '__main__':
    solve()
