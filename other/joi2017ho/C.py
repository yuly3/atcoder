import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def rot90(grid):
    h = len(grid)
    w = len(grid[0])
    res = [[0] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            res[j][h - i - 1] = grid[i][j]
    return res


def check_boundary(grid, mx_lim, mn_lim):
    h = len(grid)
    w = len(grid[0])
    cur = 0
    for i in range(h):
        for j in range(cur, w):
            if mx_lim < grid[i][j]:
                cur = j + 1
        for j in range(cur - 1, -1, -1):
            if grid[i][j] < mn_lim:
                return False
    return True


def solve():
    H, W = map(int, rl().split())
    grid0 = [list(map(int, rl().split())) for _ in range(H)]
    
    INF = 10 ** 9
    mx_a, mn_a = 0, INF
    for grid_i in grid0:
        mx_a = max(mx_a, max(grid_i))
        mn_a = min(mn_a, min(grid_i))
    
    grid1 = rot90(grid0)
    grid2 = rot90(grid1)
    grid3 = rot90(grid2)
    
    def check(t):
        mx_lim = mn_a + t
        mn_lim = mx_a - t
        if check_boundary(grid0, mx_lim, mn_lim):
            return True
        elif check_boundary(grid1, mx_lim, mn_lim):
            return True
        elif check_boundary(grid2, mx_lim, mn_lim):
            return True
        elif check_boundary(grid3, mx_lim, mn_lim):
            return True
        return False
    
    ok, ng = mx_a - mn_a, -1
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
