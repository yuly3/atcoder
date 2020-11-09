import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, N, M = map(int, rl().split())
    AB = [list(map(lambda n: int(n) - 1, rl().split())) for _ in range(N)]
    block = set()
    for _ in range(M):
        c, d = map(lambda n: int(n) - 1, rl().split())
        block.add((c, d))
    
    illuminated0 = [[False] * W for _ in range(H)]
    for a, b in AB:
        if illuminated0[a][b]:
            continue
        for j in range(b, -1, -1):
            if (a, j) in block:
                break
            illuminated0[a][j] = True
        for j in range(b + 1, W):
            if (a, j) in block:
                break
            illuminated0[a][j] = True
    
    illuminated1 = [[False] * W for _ in range(H)]
    for a, b in AB:
        if illuminated1[a][b]:
            continue
        for i in range(a, -1, -1):
            if (i, b) in block:
                break
            illuminated1[i][b] = True
        for i in range(a + 1, H):
            if (i, b) in block:
                break
            illuminated1[i][b] = True
    
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += illuminated0[i][j] | illuminated1[i][j]
    print(ans)


if __name__ == '__main__':
    solve()
