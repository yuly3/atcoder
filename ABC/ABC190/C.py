import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    AB = [list(map(lambda n: int(n) - 1, rl().split())) for _ in range(M)]
    K = int(rl())
    C, D = [], []
    for _ in range(K):
        ci, di = map(lambda n: int(n) - 1, rl().split())
        C.append(ci)
        D.append(di)
    
    pattern = []
    stack = [(0, [False] * N)]
    while stack:
        cur, p = stack.pop()
        if cur == K:
            pattern.append(p)
            continue
        p0, p1 = p[:], p[:]
        p0[C[cur]] = True
        p1[D[cur]] = True
        stack.append((cur + 1, p0))
        stack.append((cur + 1, p1))
    
    ans = 0
    for p in pattern:
        cnt = 0
        for ai, bi in AB:
            cnt += p[ai] and p[bi]
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
