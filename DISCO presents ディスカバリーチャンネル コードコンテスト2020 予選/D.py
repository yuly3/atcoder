def solve():
    m = int(input())
    dc_l = {}
    for _ in range(m):
        line = list(map(int, input().split()))
        dc_l[line[0]] = line[1]
    ans = 0


if __name__ == '__main__':
    solve()