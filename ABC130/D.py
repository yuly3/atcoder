def solve():
    N, K, *a = map(int, open(0).read().split())

    ans, a_sum, j = 0, a[0], 1
    for i in range(N):
        while a_sum < K:
            if j == N:
                break
            a_sum += a[j]
            j += 1
        if a_sum < K:
            continue
        else:
            ans += N - j + 1
            a_sum -= a[i]
    print(ans)


if __name__ == '__main__':
    solve()
