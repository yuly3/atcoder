import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  var N, M, S, T: int
  (N, M) = inputInts()
  var
    graph: array[300001, seq[int]]
    ui, vi: int
  for _ in 0..<M:
    (ui, vi) = inputInts().mapIt(it - 1)
    graph[ui].add(vi + N)
    graph[ui + N].add(vi + 2*N)
    graph[ui + 2*N].add(vi)
  (S, T) = inputInts().mapIt(it - 1)

  var
    que = initDeque[int]()
    dist: array[300001, int]
  que.addLast(S)
  dist.fill(-1)
  dist[S] = 0
  while que.len != 0:
    let cur = que.popFirst
    if cur == T:
      echo dist[cur] div 3
      quit()
    for to in graph[cur]:
      if dist[to] != -1:
        continue
      dist[to] = dist[cur] + 1
      que.addLast(to)
  echo -1
