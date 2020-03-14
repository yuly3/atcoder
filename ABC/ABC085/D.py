import sys
readline = sys.stdin.readline


def solve():
    N, H = map(int, readline().split())
    a, b = [0] * N, [0] * N
    for i in range(N):
        a[i], b[i] = map(int, readline().split())
    
    max_a = max(a)
    b.sort(reverse=True)
    ans = 0
    for i in range(N):
        if b[i] <= max_a:
            break
        H -= b[i]
        ans += 1
        if H <= 0:
            print(ans)
            exit()
    ans += H // max_a if H % max_a == 0 else H // max_a + 1
    print(ans)


if __name__ == '__main__':
    solve()
