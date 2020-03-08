import strutils, sequtils, strformat


proc solve() =
    var N, Y: int
    (N, Y) = stdin.readLine.split.map(parseInt)

    for x in 0..N:
        for y in 0..N - x:
            var d = Y - x * 10000 - y * 5000
            if d mod 1000 == 0:
                var z = d div 1000
                if x + y + z == N:
                    echo fmt"{x} {y} {z}"
                    quit()
    echo "-1 -1 -1"


when is_main_module:
    solve()
