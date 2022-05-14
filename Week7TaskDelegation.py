import queue as qu

""":cvar
Mål:
Give studerende de sværeste opgaver, når de studerende er klar.

R = ExtractMax()
N id diff = PQ.enq(id,diff)

Vi implementerer P-Q'en med en heap, da vi regner med:
N*extMax + N*insert

For sorted DL list:
N*O(1) + N*O(N) => N + N^2 = O(N^2)
For heap:
N*log(n) + N*log(n) => N*log(N) + N*log(N) = O(N*log(N))<O(N^2)

"""

N = int(input())
Q = qu.PriorityQueue()

#Data format: (N/R) ID, difficulty
for _ in range(N):
    data_recieved = input().split()
    if data_recieved[0] == "R":
        print(Q.get()[1])
    else:
        Q.put((-int(data_recieved[2]),int(data_recieved[1])))  # Vi tilføjer negativ foran difficulty, da vores PQ returner laveste først ;)


