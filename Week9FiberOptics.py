import queue as q
import collections

""":cvar
Input: n = Number of vertices

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
""":cvar
Vi bruger Kruskal's algoritme til at lave MST, der giver os den billigste sammensætning af kabler.

Trin:
1. Tag den laveste edge (p1,p2) (PQ.get())
2. Hvis denne ikke skaber en cyklus så tilføj den til træet (connected(p1,p2))
3. Gør dette, indtil vi har alle vertices i træet.

Teori:
1. Cyklus property
2. Edge property
"""
PQ = q.PriorityQueue()
sumOfWeights = 0
v_in_T = 0

N, M = tuple(map(int, input().split()))
WQU = WQU(N+1)
A = [None]*N
for x in range(N):
    A[x] = [0] #Det første index i enhver ajdacency list er lig 0

#Dataformat: B1,B2,Weight
for _ in range(M):
    data_recieved = input().split()
    B1 = int(data_recieved[0])
    B2 = int(data_recieved[1])
    w_B1B2 = int(data_recieved[2])
    PQ.put((w_B1B2,(B1,B2))) #(Weight,edge)

stopVerticesNr = N-1 #Antal vertices, før at vi har indholdt hele træet
while v_in_T != stopVerticesNr: #Så længe |V_t| != |V|
    weight,edge = PQ.get()
    if WQU.connected(edge[0],edge[1]) != True:
        WQU.union(edge[0],edge[1])
        sumOfWeights += weight
        v_in_T += 1
print(sumOfWeights)