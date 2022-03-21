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

#Singly linked Q
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

a = Node(None,1,None)
b = Node(None,2,None)
c = Node(None,3,None)
d = Node(None,4,None)
a.next = b
b.next = c


q = sLinkedQ(a)
q.enQ(d)


