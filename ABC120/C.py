def solve():
    S = input()

    zeros = S.count('0')
    ones = S.count('1')
    ans = min(zeros, ones) * 2
    print(ans)


if __name__ == '__main__':
    solve()
