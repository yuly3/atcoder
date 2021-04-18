import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](n: var T, m: T) {.inline.} = n = max(n, m)
proc chmin*[T: SomeNumber](n: var T, m: T) {.inline.} = n = min(n, m)
proc `%=`*[T: SomeInteger](n: var T, m: T) {.inline.} = n = floorMod(n, m)


type
  SquareSkipList*[T] = ref object
    square: Natural
    rand_y: int
    layer1: seq[T]
    layer0: seq[seq[T]]
    cmpFunc: (T, T) -> int

proc initSquareSkipList*[T](inf: T, cmpFunc: (T, T) -> int, square=1000, rand_y=42): SquareSkipList[T] =
  var
    layer1 = @[inf]
    layer0 = newSeqWith(1, newSeq[T]())
  return SquareSkipList[T](square: square, rand_y: rand_y, layer1: layer1, layer0: layer0, cmpFunc: cmpFunc)

proc add*[T](self: var SquareSkipList[T], x: T) =
  var y = self.rand_y
  y = y xor ((y and 0x7ffff) shl 13)
  y = y xor (y shr 17)
  y = y xor ((y and 0x7ffffff) shl 5)
  self.rand_y = y

  if floorMod(y, self.square) == 0:
    let idx1 = self.layer1.upperBound(x, self.cmpFunc)
    self.layer1.insert(@[x], idx1)
    let idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
    self.layer0.insert(self.layer0[idx1][idx0..^1], idx1 + 1)
    self.layer0[idx1].delete(idx0, self.layer0[idx1].len)
  else:
    let
      idx1 = self.layer1.upperBound(x, self.cmpFunc)
      idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
    self.layer0[idx1].insert(@[x], idx0)

proc remove*[T](self: var SquareSkipList[T], x: T) =
  let
    idx1 = self.layer1.lowerBound(x, self.cmpFunc)
    idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
  if idx0 == self.layer0[idx1].len:
    self.layer1.delete(idx1, idx1)
    self.layer0[idx1] = concat(self.layer0[idx1], self.layer0[idx1 + 1])
    self.layer0.delete(idx1 + 1, idx1 + 1)
  else:
    self.layer0[idx1].delete(idx0, idx0)

proc nextEqual*[T](self: var SquareSkipList[T], x: T): T =
  let
    idx1 = self.layer1.lowerBound(x, self.cmpFunc)
    idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
  if idx0 == len(self.layer0[idx1]):
    return self.layer1[idx1]
  return self.layer0[idx1][idx0]

proc next*[T](self: var SquareSkipList[T], x: T): T =
  let
    idx1 = self.layer1.upperBound(x, self.cmpFunc)
    idx0 = self.layer0[idx1].upperBound(x, self.cmpFunc)
  if idx0 == len(self.layer0[idx1]):
    return self.layer1[idx1]
  return self.layer0[idx1][idx0]

proc prev*[T](self: var SquareSkipList[T], x: T): T =
  let
    idx1 = self.layer1.lowerBound(x, self.cmpFunc)
    idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
  if idx0 == 0:
    return self.layer1[idx1 - 1]
  return self.layer0[idx1][idx0 - 1]

proc contains*[T](self: var SquareSkipList[T], x: T): bool =
  let
    idx1 = self.layer1.lowerBound(x, self.cmpFunc)
    idx0 = self.layer0[idx1].lowerBound(x, self.cmpFunc)
  if idx0 == self.layer0[idx1].len:
    return self.layer1[idx1] == x
  else:
    return self.layer0[idx1][idx0] == x

proc pop*[T](self: var SquareSkipList[T], idx: Natural): T =
  var
    s = -1
    i: int
  for ii, l0 in self.layer0:
    s += l0.len + 1
    i = ii
    if idx <= s:
      break
  if s == idx:
    self.layer0[i] = concat(self.layer0[i], @[self.layer0[i + 1]])
    self.layer0.delete(i + 1, i + 1)
    let res = self.layer1[i]
    self.layer1.delete(i, i)
    return res
  else:
    let res = self.layer0[i][idx - s]
    self.layer0[i].delete(idx - s, idx - s)
    return res

proc popMax*[T](self: var SquareSkipList[T]): T =
  if self.layer0[^1].len != 0:
    return self.layer0[^1].pop()
  elif 1 < self.layer1.len:
    self.layer0.delete(self.layer0.len - 1, self.layer0.len - 1)
    let res = self.layer1[^2]
    self.layer1.delete(self.layer1.len - 2, self.layer1.len - 2)
    return res
  else:
    assert(false, "This is empty")

proc `[]`*[T](self: var SquareSkipList[T], k: Natural): T =
  var
    s = -1
    ii = 0
  for i, l0 in self.layer0:
    s += l0.len + 1
    ii = i
    if k <= s:
      break
  if s == k:
    return self.layer1[ii]
  return self.layer0[ii][k - s]

proc min*[T](self: var SquareSkipList[T]): T =
  return if self.layer0[0].len != 0: self.layer0[0][0] else: self.layer1[0]

proc max*[T](self: var SquareSkipList[T]): T =
  return if self.layer0[^1].len != 0: self.layer0[^1][^1] elif 1 < self.layer1.len: self.layer1[^2] else: self.layer1[^1]


when isMainModule:
  let
    N = inputInt()
    S = inputInts()

  var ssl = initSquareSkipList(10^10, cmp[int], 513)
  ssl.add(0)
  for si in S:
    ssl.add(si)
  
  var
    children = @[ssl.popMax]
    parents: seq[int]
  for i in 0..<N:
    parents = children
    for p in parents:
      let child = ssl.prev(p)
      if child == 0:
        echo "No"
        quit()
      ssl.remove(child)
      children.add(child)
  echo "Yes"
