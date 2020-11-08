import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    xy = [list(map(int, rl().split())) for _ in range(N)]
    
    for i, (xi, yi) in enumerate(xy[:N - 2]):
        for j, (xj, yj) in enumerate(xy[i + 1:N - 1]):
            for xk, yk in xy[i + j + 2:]:
                if (yj - yi) * (xk - xi) - (xj - xi) * (yk - yi) == 0:
                    print('Yes')
                    return
    print('No')


if __name__ == '__main__':
    solve()
