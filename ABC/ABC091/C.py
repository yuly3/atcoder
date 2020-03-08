def solve():
    N = int(input())
    ab = [[] for _ in range(N)]
    cd = ab[:]
    for i in range(N):
        ab[i] = list(map(int, input().split()))
    for i in range(N):
        cd[i] = list(map(int, input().split()))
    
    ab.sort(key=lambda x: -x[0])
    cd.sort(key=lambda x: (x[0], -x[1]))
    
    ans = 0
    used = [0 for _ in range(N)]
    for i in range(N):
        use, d_min = -1, 201
        for j in range(N):
            if ab[j][0] < cd[i][0] and ab[j][1] < cd[i][1]:
                if cd[i][1] - ab[j][1] < d_min:
                    if used[j] == 0:
                        use = j
                        d_min = cd[i][1] - ab[j][1]
        if use != -1:
            used[use] = 1
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
