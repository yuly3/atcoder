def solve():
    N, M = map(int, input().split())
    
    ans = ((N - M) * 100 + M * 1900) * 2 ** M
    print(ans)


if __name__ == '__main__':
    solve()
