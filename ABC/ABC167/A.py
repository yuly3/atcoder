import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    T = rl().rstrip()
    
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
