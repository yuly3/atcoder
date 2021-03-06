import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

when is_main_module:
  var N, M, T, X, Y: int
  (N, M, T, X, Y) = inputInts()
  let p = newSeqWith(M, inputInt())

  var
    open = newSeqWith(N, newSeqWith(M, -1))
    correct = newSeqWith(N, newSeqWith(M, -1))
    incorrect = newSeqWith(N, newSeq[int](M))
    score = newSeq[int](N)

  var ti, ni, mi: int
  for _ in 0..<Y:
    let line = inputs()
    (ti, ni, mi) = line[0..2].map(parseInt)
    dec ni; dec mi
    if line[3] == "open":
      if open[ni][mi] == -1:
        open[ni][mi] = ti
    elif line[3] == "correct":
      if correct[ni][mi] == -1:
        score[ni] += max(p[mi] - (ti - open[ni][mi]) - 120*incorrect[ni][mi], X)
        correct[ni][mi] = ti
    else:
      inc incorrect[ni][mi]
  
  echo score.join("\n")
