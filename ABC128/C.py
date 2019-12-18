from itertools import combinations


def solve():
    N, M = map(int, input().split())
    k = [0 for _ in range(M)]
    s = [[] for _ in range(M)]
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
    p = list(map(int, input().split()))
    
    ans = 0
    for i in range(1, N+1):
        for on_switches in combinations(range(1, N+1), i):
            flag = True
            for j in range(M):
                count = 0
                for on_switch in on_switches:
                    if on_switch in s[j]:
                        count += 1
                if count % 2 != p[j]:
                    flag = False
                    break
            if flag:
                ans += 1
    
    if 1 not in p:
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
