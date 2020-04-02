def solve():
    H, W, N = map(int, open(0).read().split())
    bigger = max(H, W)
    print(N // bigger if N % bigger == 0 else N // bigger + 1)


if __name__ == '__main__':
    solve()
