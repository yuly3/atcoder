import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    counter = [0] * (N + 1)
    for i in range(M):
        counter[A[i]] += 1
    
    ans = 10 ** 9
    for i in range(N + 1):
        if counter[i] == 0:
            ans = i
            break
    
    for i in range(1, N - M + 1):
        counter[A[i + M - 1]] += 1
        counter[A[i - 1]] -= 1
        if counter[A[i - 1]] == 0:
            ans = min(ans, A[i - 1])
    print(ans)


if __name__ == '__main__':
    solve()
