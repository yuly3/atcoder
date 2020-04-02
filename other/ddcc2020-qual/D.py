def solve():
    M = int(input())
    d, c = [0] * M, [0] * M
    for i in range(M):
        d[i], c[i] = map(int, input().split())
    
    sum_d = 0
    for i in range(M):
        sum_d += d[i] * c[i]
    sum_c = sum(c)
    ans = (sum_c - 1) + (sum_d - 1) // 9
    print(ans)


if __name__ == '__main__':
    solve()
