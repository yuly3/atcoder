def solve():
    X = int(input())
    n = X // 100
    if X - 100 * n > 5 * n:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    solve()