from math import sqrt, factorial


def solve():
    N = int(input())
    xy_l = [[0, 0] for _ in range(N)]
    for i in range(N):
        xy_l[i] = list(map(int, input().split()))
    distance_l = []

    for i in range(N-1):
        for j in range(i+1, N):
            distance_l.append(sqrt((xy_l[i][0]-xy_l[j][0])**2 + (xy_l[i][1]-xy_l[j][1])**2))
    print(sum(distance_l)*2*factorial(N-1)/factorial(N))


if __name__ == '__main__':
    solve()