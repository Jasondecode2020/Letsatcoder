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
N = I()
nums = []
for _ in range(N):
  l, r = LI()
  nums.append((l, r))

res = [l for l, r in nums]
mn_sum = sum(res)
if mn_sum > 0:
  print('No')
  exit()
for i, (l, r) in enumerate(nums):
  d = min(0 - mn_sum, r - l)
  res[i] += d 
  mn_sum += d
  
if mn_sum == 0:
  print('Yes')
  print(' '.join([str(i) for i in res]))
else:
  print('No')