N = int(input())
H = [0] * N
S = [0] * N
for i in range(N):
    H[i], S[i] = map(int, input().split())


def calc(x):
    t = [0] * N
    for i in range(N):
        t[i] = (x - H[i]) // S[i]
    t.sort()
    res = True
    for i in range(N):
        if t[i] < i:
            res = False
            break
    return res


def solve():
    left, right = 0, 10**18
    for _ in range(100):
        mid = (left + right) // 2
        if calc(mid):
            right = mid
        else:
            left = mid
        if right - left == 1:
            break
    print(right)


if __name__ == '__main__':
    solve()
