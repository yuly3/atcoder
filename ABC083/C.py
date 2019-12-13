def solve():
    X, Y = map(int, input().split())

    ans = 0
    a = X
    while a <= Y:
        ans += 1
        a *= 2

    print(ans)


if __name__ == '__main__':
    solve()