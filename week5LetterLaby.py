

class Static_Stack:
    def __init__(self,n):
        self.list = [None]*n
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def pop(self):
        if self.top == -1:
            print("Underflow")
        else:
            self.top -= 1
            return(self.list[self.top+1])

    def push(self,x):
        if self.top == (len(self.list)-1):
            print("overflow")
        else:
            self.top += 1
            self.list[self.top] = x

class StackQueue:
    def __init__(self,n):
        self.head = Static_Stack(n)
        self.tail = Static_Stack(n)

    def dequeue(self):
        if self.tail.isEmpty():
            for _,key in enumerate(self.head.list):
                if key != None:
                    x = self.head.pop()
                    self.tail.push(x)
        self.tail.pop()

    def enqueue(self,x):
        self.head.push(x)

"""Implementering af linked lists

p = Pointer to previous element
k = Key value
n = Pointer to next element
"""
class Node:
    def __init__(self,p,k,n):
        self.key = k
        self.next = n
        self.prev = p

#Assumes nodeSequence[0] to be the head.
class sLinkedStack:
    def __init__(self,head):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def pop(self): #O(1)
        if self.isEmpty():
            print("Underflow")
            return Node(None,"Underflow",None) #So we can keep doing keys ;)
        x = self.head
        self.head = self.head.next
        return x

    def push(self,x): #O(1)
        x.next = self.head
        self.head = x

#Singly linked Q - tager nodes som input
class sLinkedQ:

    def __init__(self,head):
        self.head = sLinkedStack(head)
        self.tail = sLinkedStack(None)

    def enQ(self,x):
        self.head.push(x)

    def deQ(self):
        if self.tail.isEmpty():
            while self.head.isEmpty() == False:
                x = self.head.pop()
                self.tail.push(x)
        return self.tail.pop()

    def isEmpty(self):
        if self.head.isEmpty() and self.tail.isEmpty():
            print("Queue is empty")
            return True
        return False

"""adj simple linear-probing HashTable that uses a modulo function for assigning the places of each input.
"""
class HashTable:
    def __init__(self,divisor):
        self.divisor = divisor
        self.hashArray = [None] * self.divisor
        self.dictSize = 0 #Number of elements in the hashArray





#Slingly Linked List

""" Inserts x0 in a sorted singly listed link, where x1 is the head """
def appendInSorted(x1,x0):
    if x1.key < x0.key:
        if x0.key <= x1.next.key:
            x0.next = x1.next
            x1.next = x0
        elif x1.next is None:
            x0.next = x1
        else:
            appendInSorted(x1.next,x0)

#x0.next = x1
def invert(x0,x1):
    next = x1.next
    x1.next = x0
    if next is None:
        return x1
    else:
        invert(x1,next)

def invertSLinkyList(head):
    firstNext = head.next
    head.next = None
    x = 0
    x = invert(head,firstNext)
    return x

"""Takes an array adj of size n, creates an array B of size 2*n and inserts all elements from adj to B

B = [x1,x2,...,NONE,NONE]
"""
def dynamicResizing(ArrayA):
    ArrayB = [None]*len(ArrayA)*2
    for idx,key in enumerate(ArrayA):
        ArrayB[idx] = key
    return ArrayB

from collections import defaultdict

""" Opgave omkring at finde fra toppen af venstre hjørne til bunden af højre

Vi laver BFS, hvor en edge kun eksisterer, hvis to nodes har forskellige chars"""

"""
Mark and Q enQ'er og markerer alle nodes, som vi kan nå
"""
def markAndQ(unMarked,Q,v,marking):
    x,y,t = v.key[1],v.key[0],v.key[2]
    t += 1
    u = Node(p=v, k=[y + marking[0],x + marking[1], t], n=0)
    Q.enQ(u)
    unMarked[f"{[u.key[0],u.key[1]]}"] = False #Markerer

#finds the quickest path to the bottom starting at S
def BFS_ABA(matrix,N):
    unMarked = defaultdict(lambda: True) #Vi starter med at unmarkere alle vertices
    start = Node(p=None,k=[0,0,0],n=None) #Keyen indeholder y,x og t
    Q = sLinkedQ(None)
    Q.enQ(start)

    while Q.isEmpty() != True: #Så længe, at der er en mulig path i vores Q
        v = Q.deQ()
        x,y = v.key[1],v.key[0]
        char = matrix[y][x]  # V's bogstav
        unMarked[f"{[v.key[0], v.key[1]]}"] = False
        if (x,y) == (N-1,N-1):
            return (v.key[2]+1) #Hvis vi har nået bunden, så returner vi v's tid
        else:
            try:
                if matrix[y+1][x] != char and unMarked[f"{[y+1,x]}"]: #nedenunder
                    markAndQ(unMarked,Q,v,[1,0])
            except:
                pass
            try:
                if matrix[y][x+1] != char and unMarked[f"{[y,x+1]}"]:  # til højre for
                    markAndQ(unMarked, Q, v,[0,1])
            except:
                pass
            try:
                if y>0 and matrix[y-1][x] != char and unMarked[f"{[y-1,x]}"]: #nedenunder
                    markAndQ(unMarked,Q,v,[-1,0])
            except:
                pass
            try:
                if x>0 and matrix[y][x-1] != char and unMarked[f"{[y,x-1]}"]:  # til venstre for
                    markAndQ(unMarked,Q,v,[0,-1])
            except:
                pass
    return False #No path

N = int(input())

def getSplitList(N):
    splitList = []
    for idx in range(N):
        splitList.append(input().split())
    return splitList

def getMatrix(splitList):
    Matrix = []
    for idx, str in enumerate(splitList):
        Matrix += [list(str[0])]
    return(Matrix)

Matrix = getMatrix(getSplitList(N))
print(BFS_ABA(Matrix,N))
