def solve():
    N = int(input())
    al = list(map(lambda x: int(x) - 1, input().split()))
    bl = list(map(int, input().split()))
    cl = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        if i != N - 1:
            if al[i] + 1 == al[i + 1]:
                ans += cl[al[i]]
        ans += bl[al[i]]

    print(ans)


if __name__ == '__main__':
    solve()
