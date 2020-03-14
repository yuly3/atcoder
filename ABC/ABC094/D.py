def solve():
    _ = int(input())
    a = list(map(int, input().split()))
    
    x = max(a)
    y = 0
    min_d = 10 ** 9
    if x % 2 == 0:
        for ai in a:
            if x == ai:
                continue
            d = abs(x // 2 - ai)
            if d < min_d:
                y = ai
                min_d = d
    else:
        for ai in a:
            d = min(abs(x // 2 - ai), abs(x // 2 + 1 - ai))
            if d < min_d:
                y = ai
                min_d = d
    print(x, y)


if __name__ == '__main__':
    solve()
