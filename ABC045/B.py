from collections import deque


def next_turn(char):
    if char == 'a':
        return 0
    elif char == 'b':
        return 1
    elif char == 'c':
        return 2


def solve():
    sa = deque(list(input()))
    sb = deque(list(input()))
    sc = deque(list(input()))
    s = (sa, sb, sc)
    
    player = ['A', 'B', 'C']
    turn = 0
    while 1:
        card = s[turn].popleft()
        turn = next_turn(card)
        if not s[turn]:
            print(player[turn])
            exit()


if __name__ == '__main__':
    solve()
