import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, rl().split())
    
    ans = 10 ** 7
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i] + B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)


if __name__ == '__main__':
    solve()
