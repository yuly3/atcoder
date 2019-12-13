from math import sqrt


def solve():
    N = int(input())
    xy_l = [0 for _ in range(N)]
    for i in range(N):
        xy_l[i] = list(map(int, input().split()))
    ans = 0

    for i in range(N-1):
        for j in range(i+1, N):
            distance = sqrt((xy_l[i][0]-xy_l[j][0])**2 + (xy_l[i][1]-xy_l[j][1])**2)
            if distance > ans:
                ans = distance
    print(ans)


if __name__ == '__main__':
    solve()