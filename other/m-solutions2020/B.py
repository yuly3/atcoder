import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C = map(int, rl().split())
    K = int(rl())
    
    while K:
        if A < B:
            break
        B *= 2
        K -= 1
    while K:
        if B < C:
            break
        C *= 2
        K -= 1
    
    print('Yes' if A < B < C else 'No')


if __name__ == '__main__':
    solve()
