from collections import deque

""":cvar
Vi laver top-sort, hvor vi benytter os af en indegree liste.

Algoritmen:
1. Opret indegree listen og indegree-0-Q'en og set semester = 0
2. Tæld antallet af kurser i Q'en ved at Dq
3. Increment semestret
4. Gentag indtil, at vi har taget N kurser.
"""
"""Implementering af linked lists

p = Pointer to previous element
k = Key value
n = Pointer to next element

Brug:
Vi laver en adjecancy list som en liste adj = |V|, hvor hvert element adj[i] indeholder er en vertex.

Vertexen kan så have et array med pointers til andre vertices som sin next, således, at hvis
0-> 1 og 0->2 og 0->3
=> Node_0.n = [Node_1,Node_2,Node_3]

Dette er O(n+m) i space.
"""


class GraphNode:
    def __init__(self, k):
        self.key = k
        self.next = []


class AdjecancyList:
    def __init__(self):
        self.A = []

    def adj(self, v, u):
        v = self.A[v]
        u = self.A[u]
        for note in v.next:
            if note == u:
                return True
        return False

    def neigh(self, v):
        return len(v.next)

    # Edge = (v,u) = v -> u
    def insertEdge(self, edge):
        v = self.A[edge[0]]
        u = self.A[edge[1]]
        v.next.append(u)
        return True #Have we inserted?


class Graph:

    def __init__(self,N):
        self.N = N
        self.adj = AdjecancyList() #Vi opretter adjecancy listen
        self.Lin = [0]*(N)
        self.create_adj()
        self.Q = deque()
        self.semesters = 0
        self.courses_taken = 0

    def add_vertex(self,v):
        if self.adj[v.key] is None:
            self.adj[v.key]= v

    # Edge = (v,u) = v-> u
    def top_add_edge(self,edge): #Vi tælder indegrees
        if self.adj.insertEdge(edge):
            self.Lin[edge[1]] += 1 #Tælder indegree

    """:cvar
    1. Fjerner edgen fra vores adjacency list og memory
    2. Tælder de fjernede edges i Lin
    """
    def top_remove_node(self,v):
        #print(f"Removing: {v}")
        for neighbour in v.next: #fjerner edges og rekorder
            if self.Lin[neighbour.key] != None:
                self.Lin[neighbour.key] -= 1
        v.next = None
        self.Lin[v.key] = None
        self.adj.A[v.key] = None #Fjerner fra adj list

    """:cvar
    Finder vertices med 0-indegree og enq dem
    """
    def top_update_0in_Q(self):
        for idx,indegree in enumerate(self.Lin):
            if indegree == 0:
                #print(f"Index of indegree 0:{idx}")
                self.Q.append(self.adj.A[idx])


    def create_adj(self):
        for key in range(self.N):
            self.adj.A.append(GraphNode(k=key))

def create_Graph():
    N,M = tuple(map(int,input().split()))
    graph = Graph(N)
    for _ in range(M):
        til,fra = tuple(map(int,input().split())) #Vores edge er (u,v) => u -> v
        edge = (fra-1,til-1)
        graph.top_add_edge(edge)
    return graph


""":cvar
Vi har 3 trin:
1. Først laver vi en indegree liste, en 0-degree Q og en adjecancy list til at implementere en graph på.
2. Vi fjerner alle edges med indegree 0 og opdaterer vores indegree liste.

Hver gang vi udfører trin 2. så tæller vi, hvor mange kurser vi har taget.
3. Hvis vi har udført N kurser (Josefines behov,) så afslutter vi og returnerer antallet af semestrer det tog os.


"""
def find_semesters():
    graph = create_Graph()  # trin 1
    while graph.courses_taken < graph.N:
        graph.top_update_0in_Q() #Opdater alle 0-indegree
        graph.semesters += 1 #Rigtig rækkefølge
        while graph.Q: #Vi fjerner alle de courses vi kan tage i dette semester
            removed_vertex = graph.Q.popleft()
            graph.top_remove_node(removed_vertex)
            graph.courses_taken += 1
    return graph.semesters

print(find_semesters())
