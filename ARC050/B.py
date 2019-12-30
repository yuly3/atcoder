R, B = map(int, input().split())
x, y = map(int, input().split())


def calc(k):
    r = (R - k) // (x - 1)
    b = (B - k) // (y - 1)
    if k <= r + b:
        return True
    else:
        return False


def solve():
    left, right = 0, min(R, B) + 1
    while 1 < right - left:
        mid = (left + right) // 2
        if calc(mid):
            left = mid
        else:
            right = mid
    print(left)


if __name__ == '__main__':
    solve()
