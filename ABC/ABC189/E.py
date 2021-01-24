import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    X, Y = [0] * N, [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, rl().split())
    
    M = int(rl())
    x00, y00 = [0] * (M + 1), [0] * (M + 1)
    x01, y01 = [0] * (M + 1), [0] * (M + 1)
    x10, y10 = [0] * (M + 1), [0] * (M + 1)
    x10[0] = y01[0] = 1
    for i in range(M):
        op = rl().rstrip()
        p = 0
        if len(op) == 1:
            cmd = int(op)
        else:
            cmd, p = map(int, op.split())
        if cmd == 1:
            x00[i + 1] = y00[i]
            y00[i + 1] = -x00[i]
            x01[i + 1] = y01[i]
            y01[i + 1] = -x01[i]
            x10[i + 1] = y10[i]
            y10[i + 1] = -x10[i]
        elif cmd == 2:
            x00[i + 1] = -y00[i]
            y00[i + 1] = x00[i]
            x01[i + 1] = -y01[i]
            y01[i + 1] = x01[i]
            x10[i + 1] = -y10[i]
            y10[i + 1] = x10[i]
        elif cmd == 3:
            x00[i + 1] = 2 * p - x00[i]
            y00[i + 1] = y00[i]
            x01[i + 1] = 2 * p - x01[i]
            y01[i + 1] = y01[i]
            x10[i + 1] = 2 * p - x10[i]
            y10[i + 1] = y10[i]
        else:
            x00[i + 1] = x00[i]
            y00[i + 1] = 2 * p - y00[i]
            x01[i + 1] = x01[i]
            y01[i + 1] = 2 * p - y01[i]
            x10[i + 1] = x10[i]
            y10[i + 1] = 2 * p - y10[i]
    
    Q = int(rl())
    ans = []
    for _ in range(Q):
        a, b = map(int, rl().split())
        b -= 1
        x = (x10[a] - x00[a]) * X[b] + (x01[a] - x00[a]) * Y[b] + x00[a]
        y = (y10[a] - y00[a]) * X[b] + (y01[a] - y00[a]) * Y[b] + y00[a]
        ans.append(f'{x} {y}')
    print('\n'.join(ans))


if __name__ == '__main__':
    solve()
