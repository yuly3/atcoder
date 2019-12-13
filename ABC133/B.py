from math import sqrt


def solve():
    N, D = map(int, input().split())
    x_l = [0 for _ in range(N)]
    for i in range(N):
        x_l[i] = list(map(int, input().split()))
    ans = 0

    for i in range(N-1):
        for j in range(i+1, N):
            distance = 0
            for k in range(D):
                distance += (x_l[i][k] - x_l[j][k]) ** 2
            distance = sqrt(distance)
            if distance.is_integer():
                ans += 1

    print(ans)


if __name__ == '__main__':
    solve()