import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    for _ in range(min(K, 100)):
        imos = [0] * N
        for i in range(N):
            left = max(0, i - A[i])
            right = min(N - 1, i + A[i])
            imos[left] += 1
            if right < N - 1:
                imos[right + 1] -= 1
        for i in range(1, N):
            imos[i] += imos[i - 1]
        A = imos[:]
    print(*A)


if __name__ == '__main__':
    solve()
