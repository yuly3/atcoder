import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K, N = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    max_d = K - A[-1] + A[0]
    for i in range(1, N):
        max_d = max(max_d, A[i] - A[i - 1])
    print(K - max_d)


if __name__ == '__main__':
    solve()
