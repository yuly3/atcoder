import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    Q = int(rl())
    
    col, row = [i for i in range(N)], [i for i in range(N)]
    t_flg = 0
    ans = []
    for _ in range(Q):
        query = list(map(int, rl().split()))
        if query[0] == 1:
            _, a, b = query
            a, b = a - 1, b - 1
            if t_flg:
                mem_a, mem_b = row[a], row[b]
                row[a], row[b] = mem_b, mem_a
            else:
                mem_a, mem_b = col[a], col[b]
                col[a], col[b] = mem_b, mem_a
        elif query[0] == 2:
            _, a, b = query
            a, b = a - 1, b - 1
            if t_flg:
                mem_a, mem_b = col[a], col[b]
                col[a], col[b] = mem_b, mem_a
            else:
                mem_a, mem_b = row[a], row[b]
                row[a], row[b] = mem_b, mem_a
        elif query[0] == 3:
            t_flg ^= 1
        else:
            _, a, b = query
            a, b = a - 1, b - 1
            if t_flg:
                a, b = b, a
            c, r = col[a], row[b]
            ans.append(N * c + r)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
