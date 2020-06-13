import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    s = rl().rstrip()
    K = int(rl())
    
    ans = []
    for si in s:
        if si == 'a':
            ans.append('a')
            continue
        cnt = ord('z') - ord(si) + 1
        if cnt <= K:
            ans.append('a')
            K -= cnt
        else:
            ans.append(si)
    
    ans[-1] = chr(ord('a') + (ord(ans[-1]) - ord('a') + K % 26) % 26)
    print(''.join(ans))


if __name__ == '__main__':
    solve()
