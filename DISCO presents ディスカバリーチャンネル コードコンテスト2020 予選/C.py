def solve():
    h, w, k = map(int, input().split())
    cake = [[0 for _ in range(w)] for _ in range(h)]
    s_l = []
    a = 0
    for i in range(h):
        line = list(input())
        for j in range(w):
            if line[j] == '#':
                a += 1
                cake[i][j] = a
                s_l.append([j, i])


if __name__ == '__main__':
    solve()