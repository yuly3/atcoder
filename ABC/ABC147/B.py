def solve():
    S = list(input())
    s_reverse = S[::-1]
    ans = 0
    for i in range(len(S)):
        if S[i] != s_reverse[i]:
            ans += 1
    print(ans//2)


if __name__ == '__main__':
    solve()