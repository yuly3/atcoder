def solve():
    N, K, *a_l = map(int, open(0).read().split())
    MOD = 10**9+7
    count_a, count_b = 0, 0
    inversion = 0

    for i in range(N):
        for j in range(N):
            if a_l[i] > a_l[j]:
                if i < j:
                    count_a += 1
                count_b += 1

    inversion = count_a * K + count_b * (K * (K - 1)) // 2
    print(inversion%MOD)


if __name__ == '__main__':
    solve()