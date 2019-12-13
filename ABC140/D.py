def solve():
    N, K = map(int, input().split())
    s = input()
    count = 0

    for i in range(N - 1):
        if s[i] == s[i + 1]:
            count += 1

    print(min(count + 2 * K, N - 1))


if __name__ == '__main__':
    solve()
