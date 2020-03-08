def solve():
    N, *X = map(int, open(0).read().split())
    
    ans = 10 ** 8
    for p in range(1, 101):
        sm = 0
        for xi in X:
            sm += (xi - p) ** 2
        ans = min(ans, sm)
    print(ans)


if __name__ == '__main__':
    solve()
