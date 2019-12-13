def solve():
    N, *Ll = map(int, open(0).read().split())
    Ll.sort()
    ans = 0

    for i in range(N - 1, 0, -1):
        a = 0
        b = i - 1
        while a < b:
            if Ll[a] + Ll[b] > Ll[i]:
                ans += b - a
                b -= 1
            else:
                a += 1
    print(ans)


if __name__ == '__main__':
    solve()
