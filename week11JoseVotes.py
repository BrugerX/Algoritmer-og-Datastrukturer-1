import collections

""":cvar
Relativt simpelt: Vi havde om hashing (420, #swag) i den uge, så det er ret selvforståeligt, at vi skal bruge en dict.

Idéen er; Da en dict tager O(1) tid at finde et elements map, er det den hurtigste måde at se, om vi har rekordet noget eller ej.

Vi rekorder ved at inkrementere dict[key] += 1, hvis denne er over 0, så må dennes id være fejltalt.

Da vi kun skal tælle fejl én gang, så inkrementer vi igen, og tæller kun, når dict[key] == 1.
"""
N = int(input())
voteTracker = collections.defaultdict(lambda: 0)
miscounted = 0
for _ in range(N): #O(n)
    vote = input()
    voteTracker[vote] +=  1
    if voteTracker[vote] == 2:
        miscounted += 1

print(miscounted)