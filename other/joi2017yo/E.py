import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    grid = [[0] * W for _ in range(H)]
    pos = [0] * (H * W)
    for i in range(H):
        mi = tuple(map(int, rl().split()))
        for j in range(W):
            mij = mi[j] - 1
            grid[i][j] = mij
            pos[mij] = (i, j)
    
    ans = 0
    is_root = [False] * (H * W)
    to_sets = [-1] * (H * W)
    for num in range(H * W):
        to = set()
        cy, cx = pos[num]
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if num < grid[ny][nx]:
                    continue
                if is_root[grid[ny][nx]]:
                    is_root[num] = True
                    ans += 1
                    break
                if to_sets[grid[ny][nx]] != -1:
                    to.add(to_sets[grid[ny][nx]])
                    to_sets[num] = to_sets[grid[ny][nx]]
                if 1 < len(to):
                    is_root[num] = True
                    ans += 1
                    break
        if is_root[num]:
            continue
        if len(to) == 0:
            to_sets[num] = num
    print(ans)


if __name__ == '__main__':
    solve()
