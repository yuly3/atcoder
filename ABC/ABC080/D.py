import sys
rline = sys.stdin.readline


def solve():
    N, C = map(int, rline().split())
    schedule = [[0] * 100001 for _ in range(C)]
    for _ in range(N):
        s, t, c = map(lambda x: int(x) - 1, rline().split())
        schedule[c][s] += 1
        schedule[c][t] -= 1
    
    imos = [0] * 100001
    for ch_i in schedule:
        for i in range(100001):
            if ch_i[i] == 1:
                imos[i] += 1
            elif ch_i[i] == -1:
                imos[i + 1] -= 1
    for i in range(1, 100001):
        imos[i] += imos[i - 1]
    print(max(imos))


if __name__ == '__main__':
    solve()
