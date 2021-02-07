import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline

M = 10000


def input_float_to_int(s):
    if '.' in s:
        s0, s1 = s.split('.')
        ret = int(s0) * M
        ret += int(s1) * 10 ** (len(str(M)) - 1 - len(s1))
    else:
        ret = int(s) * M
    return ret


def int_sqrt(x):
    r = int(x ** 0.5) - 1
    while (r + 1) ** 2 <= x:
        r += 1
    return r


def solve():
    X, Y, R = map(input_float_to_int, rl().split())
    
    bottom = ((-Y + R) // M) * -M
    top = ((Y + R) // M) * M
    
    ans = 0
    for i in range(bottom, top + 1, M):
        d = R ** 2 - (Y - i) ** 2
        length = int_sqrt(d)
        right = (X + length) // M
        left = -((-X + length) // M)
        ans += right - left + 1
    print(ans)


if __name__ == '__main__':
    solve()
