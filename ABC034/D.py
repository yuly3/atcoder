N, K = map(int, input().split())
w = [0] * N
p = [0] * N
for i in range(N):
    w[i], p[i] = map(int, input().split())


def calc(t):
    d = [0] * N
    for i in range(N):
        d[i] = w[i] * (p[i] - t) / 100
    d.sort(reverse=True)
    d_sum = sum(d[:K])
    if 0 <= d_sum:
        return True
    else:
        return False


def solve():
    left, right = 0, 101
    for _ in range(100):
        mid = (left + right) / 2
        if calc(mid):
            left = mid
        else:
            right = mid
    print(left)


if __name__ == '__main__':
    solve()
