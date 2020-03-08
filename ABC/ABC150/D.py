from fractions import gcd
from functools import reduce


def lcm(x, y):
    res = (x * y) // gcd(x, y)
    if 10 ** 9 < res:
        res = 0
    return res


def solve():
    N, M, *a = map(int, open(0).read().split())
    
    half_a = [ai // 2 for ai in a]
    half_lcm = reduce(lcm, half_a)
    
    for ai in half_a:
        if (half_lcm // ai) % 2 == 0:
            print(0)
            exit()
    
    if half_lcm == 0:
        ans = 0
    else:
        ans = (M // half_lcm) - (M // (2 * half_lcm))
    print(ans)


if __name__ == '__main__':
    solve()
