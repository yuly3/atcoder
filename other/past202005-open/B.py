import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, Q = map(int, rl().split())
    
    problem_scores = [N] * M
    scores = [0] * N
    solvers = [set() for _ in range(M)]
    
    ans = []
    for _ in range(Q):
        cmd, *nm = map(int, rl().split())
        if cmd == 1:
            n = nm[0] - 1
            ans.append(scores[n])
        else:
            n, m = nm
            n, m = n - 1, m - 1
            for solver in solvers[m]:
                scores[solver] -= 1
            problem_scores[m] -= 1
            scores[n] += problem_scores[m]
            solvers[m].add(n)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
