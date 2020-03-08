def solve():
    MOD = 10 ** 9 + 7
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    row, columun = 0, 0
    ans = 1
    for i in range(N * M, 0, -1):
        in_A = i in A
        in_B = i in B
        if in_A and in_B:
            row += 1
            columun += 1
        elif in_A:
            row += 1
            ans *= columun
        elif in_B:
            columun += 1
            ans *= row
        else:
            ans *= row * columun - (N * M - i)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
