def solve():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print(N - K)


if __name__ == '__main__':
    solve()
