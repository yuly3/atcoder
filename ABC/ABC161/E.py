import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K, C = map(int, rl().split())
    S = input()
    
    left_greedy = [False] * N
    right_greedy = [False] * N
    
    i, cnt = 0, 0
    while i < N:
        if S[i] == 'o':
            cnt += 1
            left_greedy[i] = True
            i += C + 1
        else:
            i += 1
    
    if K < cnt:
        exit()
    
    i = N - 1
    while 0 <= i:
        if S[i] == 'o':
            right_greedy[i] = True
            i -= C + 1
        else:
            i -= 1
    
    for i in range(N):
        if left_greedy[i] and right_greedy[i]:
            print(i + 1)


if __name__ == '__main__':
    solve()
