from fractions import gcd


def solve():
    N, X, *x = map(int, open(0).read().split())
    
    d = [abs(X - xi) for xi in x]
    ans = d[0]
    for di in d[1:]:
        ans = gcd(ans, di)
    print(ans)


if __name__ == '__main__':
    solve()
