import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = input()
    if S[2] == S[3] and S[4] == S[5]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
