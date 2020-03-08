N, *t = map(int, open(0).read().split())
ans = 201


def calc(a, b, i):
    if i == N:
        global ans
        ans = min(ans, max(a, b))
    else:
        calc(a+t[i], b, i+1)
        calc(a, b+t[i], i+1)


def solve():
    calc(0, 0, 0)
    print(ans)


if __name__ == '__main__':
    solve()
