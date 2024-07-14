standard_input, packages = 1, 1

if 1:
  if standard_input:
    import io, os, sys
    input = lambda: sys.stdin.readline().strip()

    import math
    inf = math.inf

    def S(): # string
      return input()
    
    def I(): # int
      return int(input())

    def II(): # iterate int from a list
      return map(int, input().split())

    def LS(): # list of string
      return list(input().split())

    def LI(): # list of int
      return list(map(int, input().split()))

    def LF(): # list of float
      return list(map(float, input().split()))

    def M10(): # iterate of 1 to 0
      return map(lambda x: int(x) - 1, input().split())

    def L10(): # list of 1 to 0
      return list(map(lambda x: int(x) - 1, input().split()))

  if packages:
    import random
    import bisect
    import typing
    from collections import Counter, defaultdict, deque
    from copy import deepcopy
    from functools import cmp_to_key, lru_cache, reduce
    from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
    from itertools import accumulate, combinations, permutations, count, product
    from operator import add, iand, ior, itemgetter, mul, xor
    from string import ascii_lowercase, ascii_uppercase, ascii_letters


arr = []
N, M = LI()
A = LI()
g = defaultdict(list)
for _ in range(M):
  u, v, b = LI()
  g[u - 1].append((v - 1, b + A[v - 1]))
  g[v - 1].append((u - 1, b + A[u - 1]))

dist = [inf] * N
dist[0], q = 0 + A[0], [(0 + A[0], 0)] # cost, node
while q:
    cost, node = heappop(q)
    if cost > dist[node]:
        continue
    for nei, cost in g[node]:
        d = dist[node] + cost
        if d < dist[nei]:
            dist[nei] = d
            heappush(q, (d, nei))

for x in dist[1:]:
   arr.append(str(x))

print(' '.join(arr))