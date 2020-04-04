import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    
    rnrn = [i for i in range(1, 10)]
    
    def calc(a):
        if 3234566667 < int(a):
            return
        
        if a[-1] == '0':
            tmp = a + '0'
            rnrn.append(int(tmp))
            calc(tmp)
            tmp = a + '1'
            rnrn.append(int(tmp))
            calc(tmp)
        elif a[-1] == '9':
            tmp = a + '9'
            rnrn.append(int(tmp))
            calc(tmp)
            tmp = a + '8'
            rnrn.append(int(tmp))
            calc(tmp)
        else:
            tmp = a + str(int(a[-1]) + 1)
            rnrn.append(int(tmp))
            calc(tmp)
            tmp = a + a[-1]
            rnrn.append(int(tmp))
            calc(tmp)
            tmp = a + str(int(a[-1]) - 1)
            rnrn.append(int(tmp))
            calc(tmp)
    
    for i in range(1, 10):
        calc(str(i))
    
    rnrn.sort()
    print(rnrn[K - 1])


if __name__ == '__main__':
    solve()
