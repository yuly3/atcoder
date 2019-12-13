def solve():
    N, *bl = map(int, open(0).read().split())
    al = [0] * N
    al[0], al[-1] = bl[0], bl[-1]

    for i in range(N - 2, 0, -1):
        al[i] = min(bl[i], bl[i - 1])

    print(sum(al))


if __name__ == '__main__':
    solve()
