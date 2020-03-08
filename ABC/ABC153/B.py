def solve():
    H, N, *A = map(int, open(0).read().split())
    if sum(A) < H:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    solve()
