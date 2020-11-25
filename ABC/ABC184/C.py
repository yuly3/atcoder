import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    r1, c1 = map(int, rl().split())
    r2, c2 = map(int, rl().split())
    
    if r1 == r2 and c1 == c2:
        print(0)
        return
    
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    
    if (r1 + c1 + r2 + c2) % 2 == 0 or abs(r1 - r2) + abs(c1 - c2) <= 6 or \
       abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        return
    
    print(3)


if __name__ == '__main__':
    solve()
