def solve():
    N = int(input())
    
    if N % 2 != 0:
        print(0)
        exit()
    
    ans, denominator = 0, 10
    while denominator <= N:
        ans += N // denominator
        denominator *= 5
    print(ans)


if __name__ == '__main__':
    solve()
