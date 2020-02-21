import strutils, sequtils, math


proc solve() =
    var R, C: int
    (R, C) = stdin.readLine.split.map(parseInt)
    var grid = newSeqWith(R, stdin.readLine.split.map(parseInt))
    
    var ans = 0
    for s in 0..<2^R:
        var tmp = grid
        for i in 0..<R:
            if ((s shr i) and 1) == 1:
                for j in 0..<C:
                    tmp[i][j] = if tmp[i][j] == 1: 0 else: 1
        
        var sm = 0
        for j in 0..<C:
            var zeros, ones = 0
            for i in 0..<R:
                if tmp[i][j] == 0:
                    inc zeros
                else:
                    inc ones
            sm += max(zeros, ones)
        ans = max(ans, sm)
    echo ans


when is_main_module:
    solve()
