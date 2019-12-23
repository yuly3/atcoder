N, M = map(int, input().split())
AB = [[0, 0] for _ in range(M)]
for i in range(M):
    AB[i][0], AB[i][1] = map(int, input().split())

root = list(range(N+1))
comp_size = [1] * (N+1)


def find_root(x):
    y = root[x]
    if x == y:
        return x
    z = find_root(y)
    root[x] = z
    return z


def merge(x, y):



def solve():



if __name__ == '__main__':
    solve()
