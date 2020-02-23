def solve():
    N, K = map(int, input().split())
    div = N
    ans = 0
    while div:
        div //= K
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
