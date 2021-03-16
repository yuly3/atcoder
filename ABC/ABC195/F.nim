import algorithm, bitops, deques, heapqueue, math, sets, sequtils, strformat, strutils, sugar, tables

proc input*(): string {.inline.} = stdin.readLine
proc inputs*(): seq[string] {.inline.} = stdin.readLine.split
proc inputInt*(): int {.inline.} = stdin.readLine.parseInt
proc inputInts*(): seq[int] {.inline.} = stdin.readLine.split.map(parseInt)
proc chmax*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) {.inline.} = num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) {.inline.} = num0 = floorMod(num0, num1)

proc eratosthenes*(n: int): seq[int] =
  var
    primes = newSeq[int]()
    isPrime = newSeqWith(n + 1, true)
  isPrime[0] = false; isPrime[1] = false

  for p in 0..n:
    if not isPrime[p]:
      continue
    primes.add(p)
    for i in countup(2*p, n, p):
      isPrime[i] = false
  return primes

when is_main_module:
  var A, B: int
  (A, B) = inputInts()

  let primes = eratosthenes(72)
  var mask: array[73, int]
  for i, num in toSeq(A..B):
    for j, prime in primes:
      if num mod prime == 0:
        mask[i] = bitor(mask[i], 1 shl j)
  
  let
    N = B - A + 1
    M = len(primes)
  var dp: array[74, array[1 shl 20, int]]
  dp[0][0] = 1
  for i in 0..<N:
    for s in 0..<1 shl M:
      if bitand(s, mask[i]) == 0:
        dp[i + 1][bitor(s, mask[i])] += dp[i][s]
      dp[i + 1][s] += dp[i][s]
  echo sum(dp[N][0..<1 shl M])
