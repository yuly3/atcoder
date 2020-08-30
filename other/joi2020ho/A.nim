import algorithm, sequtils, strutils, sugar


proc bit_length(n: int): int =
  if n == 0:
    return 0
  let s = toBin(n, 60)
  return 60 - s.find('1')
 
 
type
    SegmentTree*[T] = ref object
        N0: Positive
        ide_ele: T
        data: seq[T]
        segfunc: proc (a, b: T): T
 
proc initSegmntTree*[T](size: Positive, ide_ele: T, f: proc (a, b: T): T): SegmentTree[T] =
    return SegmentTree[T](N0: 1 shl bit_length(size - 1), ide_ele: ide_ele, data: newSeqWith(2 * (1 shl bit_length(size - 1)), ide_ele), segfunc: f)
 
proc update*[T](self: var SegmentTree[T], idx: int, x: T) =
    var k = self.N0 - 1 + idx
    self.data[k] = x
    while k != 0:
        k = (k - 1) div 2
        self.data[k] = self.segfunc(self.data[k * 2 + 1], self.data[k * 2 + 2])


proc solve() =
    var
        N = stdin.readLine.parseInt
        A = stdin.readLine.split.map(parseInt)
        B = stdin.readLine.split.map(parseInt)
    
    var tie = newSeq[(int, int)]()
    for i, ai in A:
        tie.add((ai, i))
    tie.sort((a, b) => (if a[0] < b[0]: -1 elif a[0] == b[0]: 0 else: 1))
    B.sort()

    var seg_tree = initSegmntTree(N + 1, 0, (a, b) => max(a, b))
    for i in 0..<N:
        seg_tree.update(i, max(0, tie[i][0] - B[i]))
    
    var ans = newSeq[int](N + 1)
    ans[tie[^1][1]] = seg_tree.data[0]
    for i in countdown(N - 1, 0):
        seg_tree.update(i, 0)
        seg_tree.update(i + 1, max(0, tie[i + 1][0] - B[i]))
        ans[tie[i][1]] = seg_tree.data[0]
    echo ans.join(" ")


when is_main_module:
    solve()
