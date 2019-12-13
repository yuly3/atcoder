def solve():
    N, *l = map(int, open(0).read().split())

    if max(l) < sum(l) - max(l):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()