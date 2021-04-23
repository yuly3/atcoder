import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)

when isMainModule:
  var H, W: int
  (H, W) = inputInts()
  let a = newSeqWith(H, input())

  type P = tuple[y, x: int]
  var
    teleporter: array[26, seq[P]]
    s, g: P
  for i in 0..<H:
    for j in 0..<W:
      if a[i][j].isLowerAscii:
        teleporter[ord(a[i][j]) - ord('a')].add((i, j))
      elif a[i][j] == 'S':
        s = (i, j)
      elif a[i][j] == 'G':
        g = (i, j)
  
  const INF = 10^9
  var
    dist: array[2000, array[2000, int]]
    reachAlpha: array[26, bool]
    que = initDeque[P]()
  for i in 0..<H:
    dist[i].fill(INF)
  dist[s.y][s.x] = 0

  que.addLast(s)
  while que.len != 0:
    let cur = que.popFirst
    
    if a[cur.y][cur.x].isLowerAscii:
      let alpha = ord(a[cur.y][cur.x]) - ord('a')
      if not reachAlpha[alpha]:
        reachAlpha[alpha] = true
        for to in teleporter[alpha]:
          if dist[cur.y][cur.x] + 1 < dist[to.y][to.x]:
            dist[to.y][to.x] = dist[cur.y][cur.x] + 1
            que.addLast(to)
    
    for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      let to: P = (cur.y + dy, cur.x + dx)
      if 0 <= to.y and to.y < H and 0 <= to.x and to.x < W:
        if a[to.y][to.x] == '#':
          continue
        if dist[cur.y][cur.x] + 1 < dist[to.y][to.x]:
          dist[to.y][to.x] = dist[cur.y][cur.x] + 1
          que.addLast(to)
  echo if dist[g.y][g.x] != INF: dist[g.y][g.x] else: -1
