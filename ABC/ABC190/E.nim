import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when isMainModule:
  var N, M: int
  (N, M) = inputInts()
  var
    graph = newSeqWith(N, newSeq[int]())
    ai, bi: int
  for _ in 0..<M:
    (ai, bi) = inputInts()
    dec ai; dec bi
    graph[ai].add(bi)
    graph[bi].add(ai)
  let K = inputInt()
  var C = inputInts()
  C.applyIt(it - 1)

  var cToIdx = initTable[int, int]()
  for i, ci in C:
    cToIdx[ci] = i
  
  var
    dist: array[17, array[17, int]]
    searched: array[10^5, bool]
    cSet = C.toHashSet()
  const INF = 10^18
  for i in 0..<K:
    dist[i].fill(INF)
  
  for i, ci in C:
    var que = initDeque[(int, int)]()
    que.addLast((ci, 0))
    searched.fill(false)
    searched[ci] = true

    var cur, d: int
    while 0 < que.len:
      (cur, d) = que.popFirst()
      for to in graph[cur]:
        if searched[to]:
          continue
        searched[to] = true
        que.addLast((to, d + 1))
        if to in cSet:
          dist[i][cToIdx[to]] = d + 1
  
  var dp: array[2^17, array[17, int]]
  for i in 0..<2^K:
    dp[i].fill(INF)
  for i in 0..<K:
    dp[1 shl i][i] = 1

  for S in 1..<2^K:
    for i in 0..<K:
      if bitand(S shr i, 1) == 1:
        continue
      let nS = bitor(S, 1 shl i)
      for j in 0..<K:
        if i == j:
          continue
        dp[nS][i].chmin(dp[S][j] + dist[j][i])
  
  let ans = min(dp[2^K - 1])
  echo if ans != INF: ans else: -1
