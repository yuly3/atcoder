import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

proc numbering(x, y: int): int =
  let
    n = min(x, y)
    m = max(x, y)
  return m*(m - 1) div 2 + n + 1

when isMainModule:
  let N = inputInt()
  var graph: array[10^6, seq[int]]
  for i in 0..<N:
    var cur = 0
    let ai = inputInts().mapIt(it - 1)
    for aij in ai:
      let to = numbering(i, aij)
      graph[cur].add(to)
      cur = to
  
  var dist, stat: array[10^6, int]

  proc dfs(cur: int): int =
    if stat[cur] == 2:
      return dist[cur]

    var maxDist = 0
    stat[cur] = 1
    for to in graph[cur]:
      if stat[to] == 1:
        echo -1
        quit()
      maxDist.chmax(dfs(to) + 1)
    stat[cur] = 2
    dist[cur] = maxDist
    return maxDist
  
  echo dfs(0)
