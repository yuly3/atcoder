def solve():
    N, Q = map(int, input().split())
    S = input()
    l = [0 for _ in range(Q)]
    r = l[:]
    for i in range(Q):
        l[i], r[i] = map(int, input().split())
    
    ac_head = [0 for _ in range(N+1)]
    for i, char in enumerate(S[:-1]):
        if char == 'A' and S[i+1] == 'C':
            ac_head[i+1] = 1 + ac_head[i]
        else:
            ac_head[i+1] = ac_head[i]
    
    for a, b in zip(l, r):
        print(ac_head[b-1] - ac_head[a-1])


if __name__ == '__main__':
    solve()
