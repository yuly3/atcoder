P = float(input())


def calc(t):
    return t + P / 2 ** (t / 1.5)


def solve():
    high, low = 100, 0
    limit = pow(10, -9)
    while limit < high - low:
        mid_left = high / 3 + low * 2 / 3
        mid_right = high * 2 / 3 + low / 3
        if calc(mid_right) <= calc(mid_left):
            low = mid_left
        else:
            high = mid_right
    print(calc(high))


if __name__ == '__main__':
    solve()
