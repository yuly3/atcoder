import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, *ABC = map(int, rl().split())
    s = [rl().rstrip() for _ in range(N)]
    
    if sum(ABC) == 0:
        print('No')
    elif sum(ABC) == 1:
        ans = ['Yes']
        for si in s:
            idx0 = ord(si[0]) - ord('A')
            idx1 = ord(si[1]) - ord('A')
            if ABC[idx0] == 0 and ABC[idx1] == 0:
                print('No')
                return
            if ABC[idx0] == 0:
                ABC[idx0] += 1
                ABC[idx1] -= 1
                ans.append(si[0])
            else:
                ABC[idx0] -= 1
                ABC[idx1] += 1
                ans.append(si[1])
        print(*ans, sep='\n')
    else:
        if ABC[ord(s[0][0]) - ord('A')] == 0 and ABC[ord(s[0][1]) - ord('A')] == 0:
            print('No')
        else:
            ans = ['Yes']
            for i, si in enumerate(s):
                if any(num < 0 for num in ABC):
                    raise Exception
                idx0 = ord(si[0]) - ord('A')
                idx1 = ord(si[1]) - ord('A')
                if ABC[idx0] == 0:
                    ABC[idx0] += 1
                    ABC[idx1] -= 1
                    ans.append(si[0])
                elif ABC[idx1] == 0:
                    ABC[idx0] -= 1
                    ABC[idx1] += 1
                    ans.append(si[1])
                elif sum(ABC) == 2 and ABC[idx0] == 1 and ABC[idx1] == 1 and i != N - 1 and si != s[i + 1]:
                    if si[0] in s[i + 1]:
                        ABC[idx0] += 1
                        ABC[idx1] -= 1
                        ans.append(si[0])
                    else:
                        ABC[idx0] -= 1
                        ABC[idx1] += 1
                        ans.append(si[1])
                else:
                    if ABC[idx0] <= ABC[idx1]:
                        ABC[idx0] += 1
                        ABC[idx1] -= 1
                        ans.append(si[0])
                    else:
                        ABC[idx0] -= 1
                        ABC[idx1] += 1
                        ans.append(si[1])
            print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
