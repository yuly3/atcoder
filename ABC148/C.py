from fractions import gcd


def solve():
    A, B = map(int, input().split())
    
    ans = A * B / gcd(A, B)
    print(int(ans))


if __name__ == '__main__':
    solve()
