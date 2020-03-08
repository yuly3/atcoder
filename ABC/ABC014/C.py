def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    
    imos = [0] * 1000002
    for a, b in ab:
        imos[a] += 1
        imos[b + 1] -= 1
    
    for i in range(1, 1000001):
        imos[i] += imos[i - 1]
    ans = max(imos[:-1])
    print(ans)


if __name__ == '__main__':
    solve()
