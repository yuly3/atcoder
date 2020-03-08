def solve():
    N, K, *H = map(int, open(0).read().split())
    H.sort(reverse=True)
    ans = sum(H[K:])
    print(ans)


if __name__ == '__main__':
    solve()
