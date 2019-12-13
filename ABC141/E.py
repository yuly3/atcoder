def solve():
    N = int(input())
    S = input()

    ans, j = 0, 1
    for i in range(N):
        s = S[i:i+j]
        while S[i+j:].find(s) != -1:
            j += 1
            s = S[i:i+j]
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()