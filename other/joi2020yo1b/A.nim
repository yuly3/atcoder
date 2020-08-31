import algorithm, sequtils, strutils


proc solve() =
    var score = stdin.readLine.split.map(parseInt)
    score.sort()
    echo score[1] + score[2]


when is_main_module:
    solve()
