from math import sin, pi

A, B, C = map(int, input().split())


def calc(t):
    f = A * t + B * sin(C * t * pi)
    if 100 <= f:
        return True
    else:
        return False


def solve():
    left, right = 0, 10 ** 7
    for _ in range(100):
        mid = (left + right) / 2
        if calc(mid):
            right = mid
        else:
            left = mid
    print(right)


if __name__ == '__main__':
    solve()
