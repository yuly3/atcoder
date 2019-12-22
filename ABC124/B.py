def solve():
    N, *H = map(int, open(0).read().split())
    
    ans, h_max = 1, H[0]
    for i in range(1, N):
        if h_max <= H[i]:
            ans += 1
            h_max = max(h_max, H[i])
    print(ans)


if __name__ == '__main__':
    solve()
