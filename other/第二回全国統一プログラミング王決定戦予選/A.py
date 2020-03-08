def solve():
    N = int(input())
    ans = 0
    if N % 2 == 0:
        ans = N // 2 - 1
    else:
        ans = N // 2
    print(ans)


if __name__ == '__main__':
    solve()