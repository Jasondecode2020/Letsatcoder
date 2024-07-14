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


N = I()
arr = []
A = LI()
# @lru_cache(None)
def dfs(i, ans, k):
  if ans:
    d[len(ans)] += 1
  for j in range(i, N):
    if len(ans) <= 1 or A[j] + ans[-2] == 2 * ans[-1]:
      dfs(j + 1, ans + [A[j]], k + 1)
  
d = defaultdict(int)
d[-1] = inf
dfs(0, [], 0)
for i in range(1, N + 1):
  if i in d:
    arr.append(str(d[i]))
  else:
    arr.append('0')
print(' '.join(arr))