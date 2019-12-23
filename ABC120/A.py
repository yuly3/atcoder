def solve():
    A, B, C = map(int, input().split())

    ans = B // A
    if C < ans:
        ans = C
    print(ans)


if __name__ == '__main__':
    solve()
