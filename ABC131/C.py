import fractions


def solve():
    A, B, C, D = map(int, input().split())
    gcd = (C * D) // fractions.gcd(C, D)
    ans_sub = A-1 - ((A-1) // C + (A-1) // D - (A-1) // gcd)
    ans = B - (B // C + B // D - B // gcd) - ans_sub
    print(ans)


if __name__ == '__main__':
    solve()