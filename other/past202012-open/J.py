import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    X = int(rl())
    
    N = len(S)
    counter = [0] * (N + 1)
    for i, si in enumerate(S):
        if si.isdigit():
            counter[i + 1] = min(10 ** 15, counter[i] + counter[i] * int(si))
        else:
            counter[i + 1] = min(10 ** 15, counter[i] + 1)
    
    idx, c = N - 1, X
    while True:
        for i in range(idx, -1, -1):
            if counter[i] < c:
                idx = i
                break
        if S[idx].isalpha():
            print(S[idx])
            break
        c = (c - 1) % counter[idx] + 1


if __name__ == '__main__':
    solve()
