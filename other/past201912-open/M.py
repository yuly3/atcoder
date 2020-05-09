import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    AB = [list(map(int, rl().split())) for _ in range(N)]
    CD = [list(map(int, rl().split())) for _ in range(M)]
    
    def check(t):
        sorted_CD = sorted(CD, key=lambda cd: cd[0] * t - cd[1])
        used_monsters = sorted(sorted_CD[:1] + AB, key=lambda ab: ab[0] * t - ab[1])[:5]
        mass, power = 0, 0
        for m, p in used_monsters:
            mass += m
            power += p
        return mass * t <= power
    
    ok, ng = 0, 10 ** 7
    for _ in range(100):
        mid = (ok + ng) / 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
