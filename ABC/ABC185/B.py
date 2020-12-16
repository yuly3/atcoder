import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, T = map(int, rl().split())
    AB = [list(map(int, rl().split())) for _ in range(M)]
    
    battery = N
    prev_b = 0
    for a, b in AB:
        battery -= a - prev_b
        if battery <= 0:
            print('No')
            return
        battery = min(N, battery + (b - a))
        prev_b = b
    
    if T - prev_b < battery:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
