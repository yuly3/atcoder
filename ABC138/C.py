def solve():
    N, *vl = map(float, open(0).read().split())
    vl.sort()

    for _ in range(int(N) - 1):
        a, b = vl[0], vl[1]
        vl[1] = (a + b) / 2
        vl = vl[1:]

    print(vl[0])


if __name__ == '__main__':
    solve()
