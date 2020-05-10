import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, X = map(int, rl().split())
    C, A = [0] * N, [[] for _ in range(N)]
    for i in range(N):
        C[i], *Ai = map(int, rl().split())
        A[i] = Ai
    
    ans = 10 ** 18
    for s in range(1 << N):
        b = [0] * M
        c = 0
        for i in range(N):
            if s >> i & 1:
                c += C[i]
                for j in range(M):
                    b[j] += A[i][j]
        flg = True
        for i in range(M):
            if b[i] < X:
                flg = False
                break
        if flg:
            ans = min(ans, c)
    print(ans if ans != 10 ** 18 else -1)


if __name__ == '__main__':
    solve()
