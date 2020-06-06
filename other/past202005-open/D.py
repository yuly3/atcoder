import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    t = (12, 8, 11, 11, 9, 11, 12, 7, 13, 12)
    N = int(rl())
    s = [rl().rstrip() for _ in range(5)]
    
    ans = []
    for j in range(1, N + 1):
        cnt = 0
        for i in range(5):
            for k in range(1, 4):
                cnt += s[i][4 * j - k] == '#'
        for idx, val in enumerate(t):
            if cnt == val:
                if val == 12:
                    if s[3][4 * j - 3] == '.':
                        ans.append('9')
                    elif s[1][4 * j - 1] == '.':
                        ans.append('6')
                    else:
                        ans.append('0')
                elif val == 11:
                    if s[3][4 * j - 3] == '#':
                        ans.append('2')
                    elif s[1][4 * j - 3] == '#':
                        ans.append('5')
                    else:
                        ans.append('3')
                else:
                    ans.append(str(idx))
                break
    print(''.join(ans))


if __name__ == '__main__':
    solve()
