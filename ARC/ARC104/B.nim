import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

var
    counter: Table[char, int]

proc solve() =
    let
        NS = input().split
        N = NS[0].parseInt
        S = NS[1]
    
    var ans = 0
    for i in 0..<N - 1:
        counter = {'A': 0, 'T': 0, 'C': 0, 'G': 0}.toTable
        inc counter[S[i]]
        for j in i + 1..<N:
            inc counter[S[j]]
            if counter['A'] == counter['T'] and counter['C'] == counter['G']:
                inc ans
    echo ans

when is_main_module:
    solve()
