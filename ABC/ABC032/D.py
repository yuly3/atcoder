from bisect import bisect_right
from itertools import combinations


def solve():
    N, W = map(int, input().split())
    v = [0] * N
    w = [0] * N
    for i in range(N):
        v[i], w[i] = map(int, input().split())
    max_w = max(w)
    
    if N <= 30:
        first_half = N // 2
        second_half = N - first_half
        first_wv_sums = [[0, 0]]
        second_wv_sums = [[0, 0]]
        for i in range(1, first_half + 1):
            for goods in combinations(range(first_half), i):
                v_sum, w_sum = 0, 0
                for j in goods:
                    v_sum += v[j]
                    w_sum += w[j]
                if w_sum <= W:
                    first_wv_sums.append([w_sum, v_sum])
        for i in range(1, second_half + 1):
            for goods in combinations(range(first_half, N), i):
                v_sum, w_sum = 0, 0
                for j in goods:
                    v_sum += v[j]
                    w_sum += w[j]
                if w_sum <= W:
                    second_wv_sums.append([w_sum, v_sum])
        
        second_wv_sums.sort()
        m = 0
        second_v_sums = [0]
        second_w_sums = [0]
        for i in range(len(second_wv_sums)):
            if m < second_wv_sums[i][1]:
                second_w_sums.append(second_wv_sums[i][0])
                second_v_sums.append(second_wv_sums[i][1])
                m = second_wv_sums[i][1]
        
        ans = 0
        for w1, v1 in first_wv_sums:
            index = bisect_right(second_w_sums, W - w1) - 1
            ans = max(ans, v1 + second_v_sums[index])
        print(ans)
    elif max_w <= 1000:
        M = min(W + 1, sum(w) + 1)
        dp = [0] * M
        for i in range(N):
            for j in range(M - w[i] - 1, -1, -1):
                dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i])
        print(dp[-1])
    else:
        M = sum(v) + 1
        dp = [10 ** 9 + 1] * M
        dp[0] = 0
        for i in range(N):
            for j in range(M - 1, -1, -1):
                dp[j] = min(dp[j], dp[j - v[i]] + w[i])
        for i in range(M - 1, -1, -1):
            if dp[i] <= W:
                print(i)
                exit()


if __name__ == '__main__':
    solve()
