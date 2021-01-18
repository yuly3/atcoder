import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    B = list(map(int, rl().split()))
    
    if sum(ai * bi for ai, bi in zip(A, B)) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
