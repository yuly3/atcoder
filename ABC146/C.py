def solve():
    a, b, x = map(int, input().split())

    if x - a - b < 0:
        print(0)
        exit()

    if x - a*10**9 - b*10 >= 0:
        print(10**9)
        exit()

    for i in range(1, 10):
        dx = x - i * b
        ans = dx // a
        if len(str(ans)) == i:
            print(ans)
            exit()

    for i in range(1, 10):
        dx = x - i * b
        ans = dx // a
        if len(str(ans-1)) == i:
            print(ans-1)
            exit()


if __name__ == '__main__':
    solve()
