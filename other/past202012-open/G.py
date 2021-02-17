import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    
    su = sum(si.count('#') for si in S)
    
    def dfs(cy, cx, se, directions):
        flg = False
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == '#':
                if (ny, nx) in se:
                    continue
                flg = True
                dfs(ny, nx, se | {(ny, nx)}, directions + [(ny + 1, nx + 1)])
        if not flg and len(se) == su:
            print(su)
            print('\n'.join(f'{y} {x}' for y, x in directions))
            exit()
    
    for sy in range(H):
        for sx in range(W):
            if S[sy][sx] == '#':
                dfs(sy, sx, {(sy, sx)}, [(sy + 1, sx + 1)])


if __name__ == '__main__':
    solve()
