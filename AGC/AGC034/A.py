import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, A, B, C, D = map(int, rl().split())
    S = input()
    
    if C < D:
        if S[A - 1:D].find('##') == -1:
            print('Yes')
        else:
            print('No')
    else:
        if S[B - 2:D + 1].find('...') == -1:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    solve()
