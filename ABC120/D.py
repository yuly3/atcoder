N, M = map(int, input().split())
AB = [[0, 0] for _ in range(M)]
for i in range(M):
    AB[i][0], AB[i][1] = map(int, input().split())

root = list(range(N+1))
comp_size = [1] * (N+1)


def find_root(x):
    y = root[x]
    if x == y:
        return x
    z = find_root(y)
    root[x] = z
    return z


def merge(x, y):
    rx = find_root(x)
    ry = find_root(y)
    if rx == ry:
        return 0
    sx = comp_size[rx]
    sy = comp_size[ry]
    if sy < sx:
        root[ry] = rx
        comp_size[rx] += sy
    else:
        root[rx] = ry
        comp_size[ry] += sx
    return sx * sy


def solve():
    disconnect = []
    x = N * (N-1) // 2
    for a, b in AB[::-1]:
        disconnect.append(x)
        x -= merge(a, b)

    for ans in disconnect[::-1]:
        print(ans)


if __name__ == '__main__':
    solve()
