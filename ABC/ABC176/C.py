import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = 0
    for i in range(1, N):
        if A[i] < A[i - 1]:
            ans += A[i - 1] - A[i]
            A[i] = A[i - 1]
    print(ans)


if __name__ == '__main__':
    solve()
