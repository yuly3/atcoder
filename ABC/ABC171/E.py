import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = list(map(int, rl().split()))
    
    n = a[0]
    for i in range(1, N):
        n ^= a[i]
    for i in range(N):
        a[i] ^= n
    print(*a)


if __name__ == '__main__':
    solve()
