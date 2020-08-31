import sequtils, strutils, tables


proc solve() =
    var
        ABC = stdin.readLine.split.map(parseInt)
        counter = ABC.toCountTable()
    echo counter.largest().key


when is_main_module:
    solve()
