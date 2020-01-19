def solve():
    N = int(input())
    
    counter = [[0] * 10 for _ in range(10)]
    for i in range(1, N+1):
        s = str(i)
        counter[int(s[0])][int(s[-1])] += 1
    
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += counter[i][j] * counter[j][i]
    print(ans)


if __name__ == '__main__':
    solve()
