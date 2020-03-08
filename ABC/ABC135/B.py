def solve():
    _, *p_l = map(int, open(0).read().split())
    count = 0

    for i, p in enumerate(p_l):
        if i + 1 != p:
            count += 1
            if count > 2:
                print('NO')
                exit()
    print('YES')


if __name__ == '__main__':
    solve()