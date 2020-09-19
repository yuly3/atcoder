import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')


if __name__ == '__main__':
    solve()
