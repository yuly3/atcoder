def solve():
    N, *a_l = map(int, open(0).read().split())
    x_l = [0] * N

    x_l[0] = sum(a_l) - 2*(sum(a_l[1::2]))
    for i in range(1, N):
        x_l[i] = 2*a_l[i-1] - x_l[i-1]

    print(' '.join(map(str, x_l)))


if __name__ == '__main__':
    solve()