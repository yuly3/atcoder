import math


def calc(a, b, theta):
    if a * math.tan(math.radians(theta)) <= b:
        return a * a * b - a * a * a * math.tan(math.radians(theta)) / 2
    else:
        return b * b / math.tan(math.radians(theta)) * a / 2


def solve():
    a, b, x = map(int, input().split())

    ok = 90
    ng = 0
    for _ in range(1000):
        mid = (ok + ng) / 2
        if calc(a, b, mid) < x:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == '__main__':
    solve()