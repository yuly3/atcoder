def solve():
    N = int(input())
    S = input()
    ans = 1

    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()
