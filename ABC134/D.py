def solve():
    N, *a_l = map(int, open(0).read().split())
    a_l = [0] + a_l

    for i in range(N//2, 0, -1):
        a_l[i] = sum(a_l[i::i]) % 2

    b_l = [i for i, x in enumerate(a_l) if x]

    print(len(b_l))
    if len(b_l) != 0:
        print(' '.join(map(str, b_l)))


if __name__ == '__main__':
    solve()