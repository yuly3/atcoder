import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    if M == 0:
        print(1)
        return
    
    A.sort()
    if A[-1] != N:
        A.append(N + 1)
    
    sub = []
    prev_a = 0
    for ai in A:
        if ai == 1:
            prev_a = ai
            continue
        if prev_a + 1 == ai:
            prev_a = ai
            continue
        sub.append(ai - prev_a - 1)
        prev_a = ai
    
    if not sub:
        print(0)
        return
    
    size = min(sub)
    ans = 0
    for w in sub:
        ans += -(-w // size)
    print(ans)


if __name__ == '__main__':
    solve()
