def solve():
    N, K, *A = map(int, open(0).read().split())

    if (N - 1) % (K - 1) == 0:
        ans = (N - 1) // (K - 1)
    else:
        ans = (N - 1) // (K - 1) + 1
    print(ans)


if __name__ == '__main__':
    solve()
