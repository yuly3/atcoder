import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = 2 ** 30
    for S in range(2 ** (N - 1)):
        XOR = 0
        OR = 0
        for i in range(N):
            OR |= A[i]
            if S >> i & 1 or i == N - 1:
                XOR ^= OR
                OR = 0
        ans = min(ans, XOR)
    print(ans)


if __name__ == '__main__':
    solve()
