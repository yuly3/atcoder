import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  var
    graph: array[1001, seq[int]]
    ai, bi: int
  for _ in 0..<M:
    (ai, bi) = inputInts().mapIt(it - 1)
    graph[ai].add(bi)
  
  var dist: array[1001, array[1001, int]]
  for sv in 0..<N:
    var que = initDeque[int]()
    que.addLast(sv)
    var searched: array[1001, bool]
    while que.len != 0:
      let cur = que.popFirst()
      for to in graph[cur]:
        if searched[to]:
          continue
        searched[to] = true
        dist[sv][to] = dist[sv][cur] + 1
        que.addLast(to)

  let vertexes = toSeq(0..<N).filterIt(dist[it][it] != 0).sortedByIt(dist[it][it])
  if vertexes.len == 0:
    echo -1
    quit()
  
  let sv = vertexes[0]
  var
    ans = @[sv + 1]
    cur = sv
  while ans.len != dist[sv][sv]:
    for to in graph[cur]:
      if dist[cur][to] == 1 and dist[sv][to] + dist[to][sv] == dist[sv][sv]:
        cur = to
        ans.add(to + 1)
        break
  
  echo ans.len
  echo ans.join("\n")
