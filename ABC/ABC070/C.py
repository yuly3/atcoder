from fractions import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


def solve():
    N = int(input())
    ans = int(input())
    for _ in range(N - 1):
        ans = lcm(ans, int(input()))
    print(ans)


if __name__ == '__main__':
    solve()
