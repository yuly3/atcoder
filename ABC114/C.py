from collections import deque


def solve():
    N = int(input())
    
    nums = []
    que = deque([0])
    while que:
        num = que.pop()
        for c in '357':
            n_num = num*10 + int(c)
            if n_num <= N:
                if '3' in str(n_num) and '5' in str(n_num) and '7' in str(n_num):
                    nums.append(n_num)
                que.append(n_num)
    
    print(len(nums))


if __name__ == '__main__':
    solve()
