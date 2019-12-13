def solve():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    ans = 0
    for i in range(n - 1):
        if h[i + 1] <= h[i]:
            c += 1
            if c > ans:
                ans = c
        else:
            c = 0
    print(ans)


if __name__ == '__main__':
    solve()
