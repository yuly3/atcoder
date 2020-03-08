from bisect import bisect_left


def solve():
    N, *c = map(int, open(0).read().split())
    
    dp = [c[0]]
    for i in range(N):
        if dp[-1] < c[i]:
            dp.append(c[i])
        else:
            index = bisect_left(dp, c[i])
            dp[index] = c[i]
    print(N-len(dp))


if __name__ == '__main__':
    solve()
