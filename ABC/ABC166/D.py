import sys
from itertools import combinations_with_replacement

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    
    five_pow = [0]
    i = 1
    while five_pow[-1] < 10 ** 18:
        five_pow.append(i ** 5)
        i += 1
    
    for a, b in combinations_with_replacement(range(len(five_pow)), 2):
        p_of_a, p_of_b = five_pow[a], five_pow[b]
        if p_of_a - p_of_b == X:
            print(a, b)
            exit()
        if p_of_a + p_of_b == X:
            print(a, -b)
            exit()
        if p_of_b - p_of_a == X:
            print(b, a)
            exit()
        if p_of_b + p_of_a == X:
            print(b, -a)
            exit()


if __name__ == '__main__':
    solve()
