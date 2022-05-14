""":cvar
Input: n = Number of elements

Vi bruger WQU med path compression, da vi har ritti' mange finds(i,j).

Idéen er selbstverständlich, så jeg lader den være således.
"""
class WQU():
  def __init__(self, n):
    self.items = list(range(n))
    self.sizes = [1] * n
    self.count = len(self.items)

  #p,q = integers
  def union(self, p, q):
    if p == q:
      return
    p_root = self._root(p)
    q_root = self._root(q)
    if p_root == q_root:
      return

    if self.sizes[p_root] < self.sizes[q_root]:
      self.items[p_root] = q_root
      self.sizes[q_root] += self.sizes[p_root]
    else:
      self.items[q_root] = p_root
      self.sizes[p_root] += self.sizes[q_root]

    self.count -= 1

  def _root(self, p):
    root = self.items[p]
    while not root == self.items[root]:
      self.items[root] = self.items[self.items[root]]
      root = self.items[root]
    self.items[p] = root
    return root

  def find(self, p):
    return self._root(p)

  def connected(self, p, q):
    return p == q or self.find(p) == self.find(q)

  def count(self):
    return self.count


N, M = tuple(map(int, input().split()))
WQU = WQU(N)

for _ in range(M):
    data_recieved = input().split()
    c1 = int(data_recieved[1])
    c2 = int(data_recieved[2])
    if data_recieved[0] == "C":
        if WQU.connected(c1,c2):
            print("YES")
        else:
            print("NO")
    else:
        WQU.union(c1,c2)
