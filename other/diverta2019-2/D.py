import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    ga, sa, ba = map(int, rl().split())
    gb, sb, bb = map(int, rl().split())
    
    dp1 = [0] * 30000000
    dp1[0] = N
    M = N
    for i in range(N + 1):
        dp1[i + ga] = max(dp1[i + ga], dp1[i] - ga + gb)
        dp1[i + sa] = max(dp1[i + sa], dp1[i] - sa + sb)
        dp1[i + ba] = max(dp1[i + ba], dp1[i] - ba + bb)
        M = max(M, dp1[i])
    
    dp2 = [0] * 30000000
    dp2[0] = M
    ans = M
    for i in range(M + 1):
        dp2[i + gb] = max(dp2[i + gb], dp2[i] - gb + ga)
        dp2[i + sb] = max(dp2[i + sb], dp2[i] - sb + sa)
        dp2[i + bb] = max(dp2[i + bb], dp2[i] - bb + ba)
        ans = max(ans, dp2[i])
    print(ans)


if __name__ == '__main__':
    solve()
