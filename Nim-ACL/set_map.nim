when not declared ATCODER_BINARY_TREE_NODE_UTILS_HPP:
  const ATCODER_BINARY_TREE_NODE_UTILS_HPP * = 1
  type BinaryTreeNode* = concept x, type T
    x.l is T
    x.r is T
    x.p is T
  type BinaryTree* = concept x, type T
    T.Node is BinaryTreeNode
    x.root is T.Node

  proc greater_func*[K](a, b: K): bool = a < b

  proc isLeaf*[Node: BinaryTreeNode](self: Node): bool =
    return self.l == self

  proc leftMost*[Node: BinaryTreeNode](self: Node): Node =
    if self.l.isLeaf: return self
    else: return self.l.leftMost
  proc rightMost*[Node: BinaryTreeNode](self: Node): Node =
    if self.r.isLeaf: return self
    else: return self.r.rightMost
  proc parentLeft*[Node: BinaryTreeNode](node: Node): Node =
    var node = node
    while true:
      if node.p == nil: return nil
      elif node.p.l == node: return node.p
      node = node.p
  proc parentRight*[Node: BinaryTreeNode](node: Node): Node =
    var node = node
    while true:
      if node.p == nil: return nil
      elif node.p.r == node: return node.p
      node = node.p
  proc front*[Tree: BinaryTree](self: Tree): Tree.Node = self.root.leftMost
  proc tail*[Tree: BinaryTree](self: Tree): Tree.Node = self.root.rightMost
  proc begin*[Tree: BinaryTree](self: Tree): Tree.Node = self.root.leftMost

  proc succ*[Node: BinaryTreeNode](node: Node): Node =
    if not node.r.isLeaf: return node.r.leftMost
    else: return node.parentLeft
  proc pred*[Node: BinaryTreeNode](node: Node): Node =
    if not node.l.isLeaf: return node.l.rightMost
    else: return node.parentRight
  proc inc*[Node: BinaryTreeNode](node: var Node) =
    var node2 = node.succ
    swap node, node2
  proc dec*[Node: BinaryTreeNode](node: var Node) =
    var node2 = node.pred
    swap node, node2
  proc `+=`*[Node: BinaryTreeNode](node: var Node, n: int) =
    if n < 0: node -= (-n)
    for i in 0..<n: node.inc
  proc `-=`*[Node: BinaryTreeNode](node: var Node, n: int) =
    if n < 0: node += (-n)
    for i in 0..<n: node.dec

  proc index*[Node: BinaryTreeNode](t: Node): int =
    result = t.l.cnt
    var (t, p) = (t, t.p)
    while p != nil:
      if p.r == t: result += p.l.cnt + 1
      t = t.p
      p = p.p
  proc distance*[Node: BinaryTreeNode](t1, t2: Node): int =
    return t2.index - t1.index
  proc `*`*[Node: BinaryTreeNode](node: Node): auto = node.key
  iterator items*[Node: BinaryTreeNode](s: Slice[Node]): Node =
    var it = s.a
    while true:
      yield it
      if it == s.b: return
      it.inc

when not declared ATCODER_BINARY_TREE_UTILS_HPP:
  const ATCODER_BINARY_TREE_UTILS_HPP* = 1
  {.push discardable inline.}
  type SomeSortedTree* = concept x, type T
    T.Tree is BinaryTree
    T.K is typedesc
    T.V is typedesc
    T.Node is typedesc
    T.multi is typedesc
    T.p
    x.End
  type SomeSortedSet* = concept x, type T
    T is SomeSortedTree
    T.V is void
    T.multi is void
  type SomeSortedMap* = concept x, type T
    T is SomeSortedTree
    T.V isnot void
    T.multi is void
  type SomeSortedMultiSet* = concept x, type T
    T is SomeSortedTree
    T.V is void
    T.multi isnot void
  type SomeSortedMultiMap* = concept x, type T
    T is SomeSortedTree
    T.V isnot void
    T.multi isnot void
  type hasSplay* = concept x, type T
    var t: T.Node
    x.tree.splay(t)
  proc begin*[T: SomeSortedTree](self: T): T.Node = self.tree.begin()

  proc getKey*[T: SomeSortedTree](self: T, t: T.Node): auto =
    when T.V is void: t.key
    else: t.key[0]

  template calc_comp*[T: SomeSortedTree](self: T, x, y: T.K): bool =
    when T.p[0] is typeof(nil):
      x < y
    else:
      let comp = T.p[0]
      comp(x, y)

  proc lower_bound*[T: SomeSortedTree](
    self: var T, t: var T.Node, x: T.K
  ): T.Node =
    if t.isLeaf:
      return t
    if t != self.End and self.calc_comp(self.getKey(t), x):
      return self.lower_bound(t.r, x)
    else:
      var t2 = self.lower_bound(t.l, x)
      if t2.isLeaf: return t
      else: return t2

  proc lower_bound*[T: SomeSortedTree](self: var T, x: T.K): T.Node =
    assert self.tree.root != nil
    result = self.lower_bound(self.tree.root, x)
    when T is hasSplay:
      self.tree.splay(result)
      self.tree.root = result

  proc upper_bound*[T: SomeSortedTree](
    self: var T, t: var T.Node, x: T.K
  ): T.Node =
    if t.isLeaf: return t
    if t == self.End or self.calc_comp(x, self.getKey(t)):
      var t2 = self.upper_bound(t.l, x)
      if t2.isLeaf: return t
      else: return t2
    else:
      return self.upper_bound(t.r, x)

  proc upper_bound*[T: SomeSortedTree](self: var T, x: T.K): T.Node =
    assert self.tree.root != nil
    result = self.upper_bound(self.tree.root, x)
    when T is hasSplay:
      self.tree.splay(result)
      self.tree.root = result

  proc find*[T: SomeSortedTree](self: var T, x: T.K): T.Node =
    var t = self.lower_bound(x)
    if t != self.End and self.getKey(t) == x: return t
    else: return self.End

  proc contains*[T: SomeSortedTree](self: var T, x: T.K): bool =
    self.find(x) != self.End

  proc insert*[T: SomeSortedMultiSet](self: var T, x: T.K): T.Node =
    self.tree.insert(self.upper_bound(x), x)
  proc insert*[T: SomeSortedMultiMap](self: var T, x: (T.K, T.V)): T.Node =
    self.tree.insert(self.upper_bound(x[0]), x)

  proc insert*[T: SomeSortedSet](self: var T, x: T.K): T.Node =
    var t = self.lower_bound(x)
    if t != self.End and t.key == x: return t
    else: return self.tree.insert(t, x)
  proc insert*[T: SomeSortedMap](self: var T, x: (T.K, T.V)): T.Node =
    var it = self.lower_bound(x[0])
    if it != self.End and it.key[0] == x[0]: it.key[1] = x[1]; return it
    else: return self.tree.insert(it, x)
  proc incl*[T: SomeSortedSet | SomeSortedMultiSet](
    self: var T, x: T.K
  ): T.Node =
    self.insert(x)
  proc incl*[T: SomeSortedMap | SomeSortedMultiMap](
    self: var T, x: (T.K, T.V)
  ): T.Node =
    self.insert(x)

  template getAddr*[T: SomeSortedMap](self: var T, x: T.K): auto =
    mixin default
    var t = self.lower_bound(x)
    if t == self.End or t.key[0] != x:
      var v = T.V.default
      t = self.tree.insert(t, (x, v))
    t.key[1].addr

  template `[]`*[T: SomeSortedMap](self: var T, x: T.K): auto =
    var t = self.getAddr(x)
    t[]
  proc `[]=`*[T: SomeSortedMap](self: var T, x: T.K, v: T.V) =
    var t = self.getAddr(x)
    t[] = v

  proc erase*[T: SomeSortedTree](self: var T, x: T.K): T.Node =
    mixin erase
    var t = self.lower_bound(x)
    if t == self.End or self.getKey(t) != x: return self.End
    else: return self.tree.erase(t)
  proc erase*[T: SomeSortedTree](self: var T,
      t: T.Node): T.Node = self.tree.erase(t)
  proc excl*[T: SomeSortedTree](self: var T, x: T.K): T.Node = self.erase(x)
  proc excl*[T: SomeSortedTree](self: var T, t: T.Node): T.Node = self.erase(t)

  proc kth_element*[T: SomeSortedTree](self: var T, t: T.Node, k: int): T.Node =
    let p = t.l.cnt
    if k < p: return self.kth_element(t.l, k)
    elif k > p: return self.kth_element(t.r, k - p - 1)
    else: return t

  proc kth_element*[T: SomeSortedTree](self: var T, k: int): T.Node =
    return self.kth_element(self.tree.root, k)
  proc `{}`*[T: SomeSortedTree](self: var T, k: int): T.Node =
    return self.kth_element(k)

  proc index*[T: SomeSortedTree](self: T, t: T.Node): int =
    # static:
      # assert T.Tree.Countable isnot void
    return index(t)
  proc distance*[T: SomeSortedTree](self: T, t1, t2: T.Node): int =
    # static:
      # assert T.Tree.Countable isnot void
    return index(t2) - index(t1)

  iterator items*[T: SomeSortedSet or SomeSortedMultiSet](self: T): T.K =
    var it = self.begin
    while it != self.End:
      yield it.key
      it.inc
  iterator pairs*[T: SomeSortedMap or SomeSortedMultiMap](self: T): (T.K, T.V) =
    var it = self.begin
    while it != self.End:
      yield it.key
      it.inc
  proc `end`*[Tree: SomeSortedTree](self: Tree): Tree.Node = self.End
    {.pop.}

when not declared ATCODER_RED_BLACK_TREE_HPP:
  const ATCODER_RED_BLACK_TREE_HPP* = 1
  import std/sugar
  #  {.experimental: "codeReordering".}
  {.push inline, discardable.}
  type
    Color* = enum red, black
    RedBlackTreeNode*[K; Countable] = ref object
      p*, l*, r*: RedBlackTreeNode[K, Countable]
      key*: K
      color*: Color
      id*: int
      when Countable isnot void:
        cnt*: int
    RedBlackTreeType*[K, Node; Countable] = object of RootObj
      root*, leaf*: Node
      size*: int
      next_id*: int
    RedBlackTree*[K; Countable] = RedBlackTreeType[
      K, RedBlackTreeNode[K, Countable], Countable
    ]

  proc newNode[T: RedBlackTree](self: var T, parent: T.Node): T.Node =
    result = T.Node(
      p: parent, l: self.leaf, r: self.leaf, color: Color.red, id: self.next_id
    )
    when T.Countable isnot void:
      result.cnt = 1

  proc newNode[T: RedBlackTree](self: var T, parent: T.Node, key: T.K): T.Node =
    result = self.newNode(parent)
    result.key = key
    self.next_id += 1
  proc init*[T: RedBlackTree](self: var T, root: var T.Node) =
    self.leaf = self.Node(color: Color.black, id: -1)
    self.leaf.l = self.leaf
    self.leaf.r = self.leaf
    when T.Countable isnot void:
      self.leaf.cnt = 0
    if root != nil:
      self.root = root
      self.root.l = self.leaf
      self.root.r = self.leaf
      self.root.p = nil
      self.root.color = Color.black
    self.next_id = 0

  template update*[T: RedBlackTree](self: T, node: T.Node) =
    when T.Countable isnot void:
      if node == self.leaf or node == nil: return
      node.cnt = node.l.cnt + node.r.cnt
      node.cnt.inc
    discard

  proc rotateLeft[T: RedBlackTree](self: var T, parent: T.Node) =
    if parent == nil: return
    var right = parent.r
    parent.r = right.l
    if right.l != self.leaf: right.l.p = parent
    right.p = parent.p
    if parent.p == nil: self.root = right
    elif parent.p.l == parent: parent.p.l = right
    else: parent.p.r = right
    right.l = parent
    parent.p = right
    self.update(parent)
    self.update(right)

  proc rotateRight[T: RedBlackTree](self: var T, parent: T.Node) =
    if parent == nil: return
    var left = parent.l
    parent.l = left.r
    if left.r != self.leaf: left.r.p = parent
    left.p = parent.p
    if parent.p == nil: self.root = left
    elif parent.p.r == parent: parent.p.r = left
    else: parent.p.l = left
    left.r = parent
    parent.p = left
    self.update(parent)
    self.update(left)

  # insert {{{
  proc fixInsert[T: RedBlackTree](self: var T, node: T.Node) =
    ## Rebalances a tree after an insertion
    if T.Countable isnot void:
      var curr = node
      while curr != nil:
        self.update(curr)
        curr = curr.p

    var curr = node
    while curr != self.root and curr.p.color == Color.red:
      if curr.p.p != nil and curr.p == curr.p.p.l:
        var uncle = curr.p.p.r
        if uncle.color == Color.red:
          curr.p.color = Color.black
          uncle.color = Color.black
          curr.p.p.color = Color.red
          curr = curr.p.p
        else:
          if curr == curr.p.r:
            curr = curr.p
            self.rotateLeft(curr)
          curr.p.color = Color.black
          if curr.p.p != nil:
            curr.p.p.color = Color.red
            self.rotateRight(curr.p.p)
      elif curr.p.p != nil:
        var uncle = curr.p.p.l
        if uncle.color == Color.red:
          curr.p.color = Color.black
          uncle.color = Color.black
          curr.p.p.color = Color.red
          curr = curr.p.p
        else:
          if curr == curr.p.l:
            curr = curr.p
            self.rotateRight(curr)
          curr.p.color = Color.black
          if curr.p.p != nil:
            curr.p.p.color = Color.red
            self.rotateLeft(curr.p.p)
    self.root.color = Color.black


  proc insert*[T: RedBlackTree](
    self: var T, node: T.Node, next: T.Node
  ): T.Node {.discardable.} =
    self.size += 1
    if next.l == self.leaf:
      # insert at next.l
      next.l = node
      node.p = next
    else:
      var curr = next.l.rightMost
      # insert at curr.r
      curr.r = node
      node.p = curr
    self.fixInsert(node)
    return node

  proc insert*[T: RedBlackTree](self: var T, next: T.Node, x: T.K): T.Node {.discardable.} =
    var node = self.newNode(T.Node(nil), x)
    return self.insert(node, next)
  # }}}

  # erase {{{
  proc fixErase*[T: RedBlackTree](self: var T, node: T.Node, parent: T.Node) =

    var
      child = node
      parent = parent
    while child != self.root and child.color == Color.black:
      if parent == nil: break # add!!!!!!!!
      if child == parent.l:
        var sib = parent.r
        if sib.color == Color.red:
          sib.color = Color.black
          parent.color = Color.red
          self.rotateLeft(parent)
          sib = parent.r

        if sib.l.color == Color.black and sib.r.color == Color.black:
          sib.color = Color.red
          child = parent
          parent = child.p
        else:
          if sib.r.color == Color.black:
            sib.l.color = Color.black
            sib.color = Color.red
            self.rotateRight(sib)
            sib = parent.r
          sib.color = parent.color
          parent.color = Color.black
          sib.r.color = Color.black
          self.rotateLeft(parent)
          child = self.root
          parent = child.p
      else:
        var sib = parent.l
        if sib.color == Color.red:
          sib.color = Color.black
          parent.color = Color.red
          self.rotateRight(parent)
          sib = parent.l

        if sib.r.color == Color.black and sib.l.color == Color.black:
          sib.color = Color.red
          child = parent
          parent = child.p
        else:
          if sib.l.color == Color.black:
            sib.r.color = Color.black
            sib.color = Color.red
            self.rotateLeft(sib)
            sib = parent.l
          sib.color = parent.color
          parent.color = Color.black
          sib.l.color = Color.black
          self.rotateRight(parent)
          child = self.root
          parent = child.p
    child.color = Color.black

  proc write*[T: RedBlackTree](rbt: T, self: T.Node, h = 0) =
    for i in 0..<h: stderr.write " | "
    if self == rbt.leaf:
      stderr.write "*\n"
    else:
      stderr.write "id: ", self.id, " key: ", self.key, " color: ", self.color
      when T.Countable isnot void:
        stderr.write " cnt: ", self.cnt, " "
        # if self.key == T.K.inf: stderr.write "inf"
    if self.p != nil: stderr.write " parent: ", self.p.id
    else: stderr.write " parent: nil"
    stderr.write "\n"
    if h >= 5:
      stderr.write "too deep!!!\n"
      assert false
      return
    rbt.write(self.l, h + 1)
    rbt.write(self.r, h + 1)

  proc write*[T: RedBlackTree](self: T) =
    stderr.write "======= RB-TREE =============\n"
    self.write(self.root, 0)
    stderr.write "======= END ==========\n"
  proc checkTree*[T: RedBlackTree](self: T) =
    doAssert self.root.color == Color.black
    var black_ct_s = initHashSet[int]()
    proc checkTreeSub(node: T.Node, black_ct: int) =
      var black_ct = black_ct
      if node.color == Color.black: black_ct.inc
      if node == self.leaf:
        black_ct_s.incl(black_ct)
        return
      if node.color == Color.red:
        doAssert node.l.color == Color.black and node.r.color == Color.black
      checkTreeSub(node.l, black_ct)
      checkTreeSub(node.r, black_ct)
    checkTreeSub(self.root, 0)
    doAssert black_ct_s.len == 1


  proc erase*[T: RedBlackTree](self: var T, node: T.Node): T.Node =
    var node = node
    self.size.dec
    var succ = node.succ
    if node.l != self.leaf and node.r != self.leaf:
      swap(node.color, succ.color)
      when T.Countable isnot void:
        swap(node.cnt, succ.cnt)
      # swap node and succ
      if node.r == succ:
        let tmp = succ.l
        succ.l = node.l
        if node.l != self.leaf:
          node.l.p = succ
        if node.r != self.leaf:
          node.r.p = succ
        node.l = tmp
        node.r = succ.r
        succ.r = node
        succ.p = node.p
        node.p = succ
        if succ.p != nil:
          if succ.p.l == node:
            succ.p.l = succ
          if succ.p.r == node:
            succ.p.r = succ
      else:
        swap(node.p, succ.p)
        swap(node.l, succ.l)
        swap(node.r, succ.r)
        if node.p != nil:
          if node.p.l == succ:
            node.p.l = node
          if node.p.r == succ:
            node.p.r = node
        if node.l != self.leaf:
          node.l.p = node
        if node.r != self.leaf:
          node.r.p = node
        if succ.p != nil:
          if succ.p.l == node:
            succ.p.l = succ
          if succ.p.r == node:
            succ.p.r = succ
        if succ.l != self.leaf:
          succ.l.p = succ
        if succ.r != self.leaf:
          succ.r.p = succ
      if self.root == node:
        self.root = succ

    #    self.write()
    #    node.key = pred.key
    #    node.value = pred.value
    #    node = pred
    when T.Countable isnot void:
      proc update_parents(self: T, node: T.Node) =
        var curr = node
        while curr != nil:
          self.update(curr)
          curr = curr.p

    let child = if node.l != self.leaf: node.l else: node.r
    if child != self.leaf:
      child.p = node.p
      if node.p == nil:
        self.root = child
      elif node == node.p.l:
        node.p.l = child
      else:
        node.p.r = child
      when T.Countable isnot void:
        self.update_parents(node.p)
      if node.color == Color.black:
        self.fixErase(child, node.p)
    else:
      if node.p == nil:
        self.root = self.leaf
      elif node == node.p.l:
        node.p.l = self.leaf
      else:
        assert node == node.p.r
        node.p.r = self.leaf
      when T.Countable isnot void:
        self.update_parents(node.p)
      if node.color == Color.black:
        self.fixErase(self.leaf, node.p)
    return succ
  # }}}

  proc len*[T: RedBlackTree](self: T): int =
    return self.size
  proc empty*[T: RedBlackTree](self: T): bool =
    return self.len == 0

  iterator iterOrder*[T: RedBlackTree](self: T): auto =
    var node = self.root
    var stack: seq[T.Node] = @[]
    while stack.len() != 0 or node != self.leaf:
      if node != self.leaf:
        stack.add(node)
        node = node.l
      else:
        node = stack.pop()
        if node == self.End: break
        yield node.key
        node = node.r
  {.pop.}

when not declared ATCODER_SET_MAP_HPP:
  const ATCODER_SET_MAP_HPP* = 1
  #type BinaryTreeType = enum
  #  RedBlack,
  #  Splay,
  #  Randomized
  #const SetMapType = BinaryTreeType.RedBlack
  # red black
  const USE_RED_BLACK_TREE = true
  const USE_SPLAY_TREE = false
  # splay
  #  const USE_RED_BLACK_TREE = false
  #  const USE_SPLAY_TREE = true
  # RBST
  #  const USE_RED_BLACK_TREE = false
  #  const USE_SPLAY_TREE = false

  {.push discardable inline.}
  import std/strutils
  type MULTI_TRUE = int32
  type MULTI_FALSE = void
  type SortedTree*[Tree, Node, multi, K, V; p: static[tuple]] = object
    tree*: Tree
    End*: Node

  when USE_RED_BLACK_TREE:
    type
      SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[
        RedBlackTree[K, Countable],
        RedBlackTreeNode[K, Countable],
        MULTI_FALSE,
        K,
        void,
        p
      ]
      SortedMultiSetType*[K; Countable; p: static[tuple]] = SortedTree[
        RedBlackTree[K, Countable],
        RedBlackTreeNode[K, Countable],
        MULTI_TRUE,
        K,
        void,
        p
      ]
      SortedMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[
        RedBlackTree[(K, V), Countable],
        RedBlackTreeNode[(K, V), Countable],
        MULTI_FALSE,
        K,
        V,
        p
      ]
      SortedMultiMapType*[
        K; V: not void; Countable; p: static[tuple]
      ] = SortedTree[
        RedBlackTree[(K, V), Countable],
        RedBlackTreeNode[(K, V), Countable],
        MULTI_TRUE,
        K,
        V,
        p
      ]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType
    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      type Node = Tree.Node
      var End = Node(id: -2)
      when Tree.Tree.Countable isnot void:
        End.cnt = 1
      self.End = End
      self.tree.init(End)
    proc empty*[Tree: SetOrMap](self: Tree): bool = self.tree.empty()
    proc len*[Tree: SetOrMap](self: Tree): int = self.tree.len()
  elif USE_SPLAY_TREE:
    include atcoder/extra/structure/splay_tree
    type
      SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[
        SplayTree[K],
        SplayTreeNode[K, void, void, void],
        MULTI_FALSE,
        K,
        void,
        p
      ]
      SortedMultiSetType*[K; Countable; p: static[tuple]] = SortedTree[
        SplayTree[K],
        SplayTreeNode[K, void, void, void],
        MULTI_TRUE,
        K,
        void,
        p
      ]
      SortedMapType*[K; V: not void; Countable; p: static[tuple]] = SortedTree[
        SplayTree[(K, V)],
        SplayTreeNode[(K, V), void, void, void],
        MULTI_FALSE, K, V, p
      ]
      SortedMultiMapType*[
        K; V: not void; Countable; p: static[tuple]
      ] = SortedTree[
        SplayTree[(K, V)],
        SplayTreeNode[(K, V), void, void, void],
        MULTI_TRUE,
        K,
        V,
        p
      ]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType
    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      var End = Tree.Node(id: -2)
      End.cnt = 1 # be carefull!!!!!!!!!!!!!!!
      self.End = End
      self.tree.init(End)
    proc len*[Tree: SetOrMap](self: Tree): int = self.tree.root.cnt - 1
    proc empty*[Tree: SetOrMap](self: Tree): bool = self.len == 0

  else:
    include atcoder/extra/structure/randomized_binary_search_tree_with_parent

    type SortedSetType*[K; Countable; p: static[tuple]] = SortedTree[
      RandomizedBinarySearchTree[K],
      RandomizedBinarySearchTree[K].Node,
      MULTI_FALSE,
      K,
      void,
      p
    ]
    type SortedMultiSetType*[K, Countable; p: static[tuple]] = SortedTree[
      RandomizedBinarySearchTree[K],
      RBSTNode[K, void, void],
      MULTI_TRUE,
      K,
      void,
      p
    ]
    type SortedMapType*[K, V, Countable; p: static[tuple]] = SortedTree[
      RandomizedBinarySearchTree[(K, V)],
      RBSTNode[(K, V), void, void],
      MULTI_FALSE,
      K,
      V,
      p
    ]
    type SortedMultiMapType*[K, V, Countable; p: static[tuple]] = SortedTree[
      RandomizedBinarySearchTree[(K, V)],
      RBSTNode[(K, V), void, void],
      MULTI_TRUE,
      K,
      V,
      p
    ]

    type SetOrMap = SortedMultiSetType or SortedSetType or SortedMultiMapType or SortedMapType

    proc init*[Tree: SetOrMap](self: var Tree) =
      when Tree.V is void:
        type T = Tree.K
      else:
        type T = (Tree.K, Tree.V)
      var End = Tree.Node(id: -2)
      End.cnt = 1 # be carefull!!!!!!!!!!!!!!!
      self.End = End
      self.tree.init(End)

    proc len*[Tree: SetOrMap](self: Tree): int = self.tree.len() - 1
    proc empty*[Tree: SetOrMap](self: Tree): bool = self.len() == 0

  {.pop.}
  proc check_tree*(self: SetOrMap) = self.tree.check_tree

  template SortedSet*(
    K: typedesc;
    countable: static[bool] = false;
    comp: static[proc(a, b: K): bool] = nil
  ): typedesc =
    SortedSetType[K, when countable: int else: void, (comp, )]
  template SortedMultiSet*(
    K: typedesc;
    countable: static[bool] = false;
    comp: static[proc(a, b: K): bool] = nil
  ): typedesc =
    SortedMultiSetType[K, when countable: int else: void, (comp, )]
  template SortedMap*(
    K: typedesc;
    V: typedesc[not void];
    countable: static[bool] = false;
    comp: static[proc(a, b: K): bool] = nil
  ): typedesc =
    SortedMapType[K, V, when countable: int else: void, (comp, )]
  template SortedMultiMap*(
    K: typedesc;
    V: typedesc[not void];
    countable: static[bool] = false;
    comp: static[proc(a, b: K): bool] = nil
  ): typedesc =
    SortedMultiMapType[K, V, when countable: static[bool] = false, (comp, )]

  proc default*[T: SetOrMap](self: typedesc[T]): T =
    result.init()
  template initSortedSet*[K](
    countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil
  ): auto =
    block:
      var r: SortedSetType[K, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMultiSet*[K](
    countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil
  ): auto =
    block:
      var r: SortedMultiSetType[K, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMap*[K; V: not void](
    countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil
  ): auto =
    block:
      var r: SortedMapType[K, V, when countable: int else: void, (comp, )]
      r.init()
      r
  template initSortedMultiMap*[K; V: not void](
    countable: static[bool] = false; comp: static[proc(a, b: K): bool] = nil
  ): auto =
    block:
      var r: SortedMultiMapType[K, V, when countable: int else: void, (comp, )]
      r.init()
      r

  proc `$`*(self: SetOrMap): string =
    var a = newSeq[string]()
    var node = self.tree.root
    var stack: seq[self.Node] = @[]
    while stack.len() != 0 or not node.isLeaf:
      if not node.isLeaf:
        if node != self.End:
          stack.add(node)
        node = node.l
      else:
        node = stack.pop()
        when self.V is void:
          var k = ""
          k.addQuoted(node.key)
          a &= k
        else:
          var k, v = ""
          k.addQuoted(node.key[0])
          v.addQuoted(node.key[1])
          a &= k & ": " & v
        node = node.r
    return "{" & a.join(", ") & "}"
