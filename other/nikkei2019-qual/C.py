import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, rl().split())
    
    d = [0] * N
    for i in range(N):
        d[i] = A[i] + B[i]
    d.sort(reverse=True)
    
    ans = sum(d[::2]) - sum(B)
    print(ans)


if __name__ == '__main__':
    solve()
