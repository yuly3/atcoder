import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C = map(int, rl().split())
    
    if A < B:
        print('Aoki')
    elif B < A:
        print('Takahashi')
    elif C == 0:
        print('Aoki')
    else:
        print('Takahashi')


if __name__ == '__main__':
    solve()
