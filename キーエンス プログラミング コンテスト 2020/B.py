from operator import itemgetter


def solve():
    N = int(input())
    XL = [[] for _ in range(N)]
    for i in range(N):
        XL[i] = list(map(int, input().split()))
    
    XL.sort(key=itemgetter(0))
    ans = N
    r = sum(XL[0])
    for i in range(1, N):
        if XL[i][0] - XL[i][1] < r:
            ans -= 1
            r = min(r, sum(XL[i]))
        else:
            r = sum(XL[i])
    print(ans)


if __name__ == '__main__':
    solve()
