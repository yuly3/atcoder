def solve():
    N, K, S = map(int, input().split())
    if S == 10 ** 9:
        ans = [S for _ in range(K)] + [1 for _ in range(N - K)]
    else:
        ans = [S for _ in range(K)] + [S + 1 for _ in range(N - K)]
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()
