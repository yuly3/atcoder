def solve():
    N = int(input())
    S = input()
    ans = 0

    for i in range(10):
        s1 = S.find(str(i), 0, -2)
        if s1 == -1:
            continue
        for j in range(10):
            s2 = S.find(str(j), s1+1, -1)
            if s2 == -1:
                continue
            ans += len(set(S[s2+1:]))
    print(ans)


if __name__ == '__main__':
    solve()